cmake_minimum_required(VERSION 3.10)
project(AgentClient
        VERSION 0.1.0
        DESCRIPTION "FIRASIM C++ Agent Client"
        LANGUAGES CXX)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

set(GRPC_GENERATE_CPP_APPEND_PATH OFF)
set(GRPC_IMPORT_DIRS "${CMAKE_CURRENT_LIST_DIR}/FIRAMessage")
find_package(Protobuf 3 REQUIRED)
find_package(gRPC REQUIRED)
if(WIN32)
    # Needed only on windows
    find_package(ZLIB REQUIRED)
    find_package(c-ares REQUIRED)
    find_package(WS2_32 REQUIRED)
    find_library(ADDRESS_SORTING_LIB address_sorting)
endif()

# Add command option parser
add_subdirectory(third_party/CLI11)

# Generate config file
configure_file(
        include/config.h.in
        ${PROJECT_BINARY_DIR}/config.h)

# Find All proto defination
file(GLOB_RECURSE PROTO_FILES "FIRAMessage/*.proto")

#To generate gRPC C++ sources: ${GRPC_SRCS}
#To generate gRPC C++ headers: ${GRPC_HDRS}
grpc_generate_cpp(GRPC_SRCS GRPC_HDRS ${PROTO_FILES})

option(USE_CLANG_TIDY "Use clang-tidy" OFF)
if(USE_CLANG_TIDY)
    set(CMAKE_CXX_CLANG_TIDY "clang-tidy")
endif()

# Suppress warnings for external headers in MSVC
if (MSVC AND CMAKE_CXX_COMPILER_VERSION VERSION_GREATER_EQUAL 19.14)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /experimental:external /external:W0 ")
    set(CMAKE_INCLUDE_SYSTEM_FLAG_CXX "/external:I ")
endif()

add_library(generated_proto
        ${GRPC_SRCS}
        ${GRPC_HDRS})
target_include_directories(generated_proto SYSTEM PUBLIC
        ${PROJECT_BINARY_DIR}
        ${GRPC_INCLUDE_DIRS})
set_target_properties(generated_proto PROPERTIES
        CXX_CLANG_TIDY "")
if(WIN32)
    target_compile_definitions(generated_proto PUBLIC
            "-D_WIN32_WINNT=0x0A00")
endif()
if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    # Suppress all warnings when compiling generated files
    target_compile_options(generated_proto PRIVATE
            "/W0")
endif()

add_executable(AgentClient
        config.h
        include/platform.h
        src/main.cpp
        src/cpp_strategy.cpp
        include/cpp_strategy.h
        src/strategy_server.cpp
        include/strategy_server.h
        src/convert.cpp
        include/convert.h)

target_include_directories(AgentClient PRIVATE
        include)
target_link_libraries(AgentClient PRIVATE
        generated_proto
        CLI11::CLI11
        protobuf::libprotobuf
        gRPC::grpc
        gRPC::grpc++
        ${CMAKE_DL_LIBS})
if(WIN32)
    target_link_libraries(AgentClient PRIVATE
            ZLIB::ZLIB
            c-ares::cares
            WS2_32::WS2_32
            ${ADDRESS_SORTING_LIB})
endif()

if((CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
        AND CMAKE_CXX_COMPILER_VERSION VERSION_LESS 9.0)
    target_link_libraries(AgentClient PRIVATE stdc++fs)
endif()

if(CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    target_compile_options(AgentClient PRIVATE -Wall -Wextra)
endif()

target_compile_features(AgentClient PRIVATE cxx_std_17)
if(CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    # Use C++20 in MSVC for designated initializers
    set_target_properties(AgentClient PROPERTIES
            CXX_STANDARD 20
            CXX_STANDARD_REQUIRED ON)
endif()
