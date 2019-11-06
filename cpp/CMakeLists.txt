cmake_minimum_required(VERSION 3.15)
project(AgentClient
        VERSION 0.1.0
        DESCRIPTION "FIRASIM C++ Agent Client"
        LANGUAGES CXX)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")

set(PROTOBUF_GENERATE_CPP_APPEND_PATH OFF)
set(GRPC_GENERATE_CPP_APPEND_PATH OFF)
set(Protobuf_IMPORT_DIRS "${CMAKE_CURRENT_LIST_DIR}/FIRAMessage")
set(GRPC_IMPORT_DIRS "${CMAKE_CURRENT_LIST_DIR}/FIRAMessage")
find_package(Protobuf 3 REQUIRED)
find_package(gRPC REQUIRED)
message(STATUS "Using Protobuf ${Protobuf_VERSION}")
message(STATUS "Using gRPC ${GRPC_VERSION}")

# Add command option parser
add_subdirectory(CLI11)

# Generate config file
configure_file(
        include/config.h.in
        ${PROJECT_BINARY_DIR}/config.h)

file(GLOB_RECURSE PROTO_FILES "FIRAMessage/*.proto")
message(STATUS "Found Proto files: ${PROTO_FILES}")

#protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${PROTO_FILES})
grpc_generate_cpp(GRPC_SRCS GRPC_HDRS ${PROTO_FILES})
message(STATUS "To generate gRPC C++ sources: ${GRPC_SRCS}")
message(STATUS "To generate gRPC C++ headers: ${GRPC_HDRS}")

add_executable(AgentClient
        config.h
        ${GRPC_SRCS}
        ${GRPC_HDRS}
        include/platform.h
        src/main.cpp
        src/cpp_strategy.cpp
        include/cpp_strategy.h
        src/strategy_server.cpp
        include/strategy_server.h)

target_include_directories(AgentClient PRIVATE
        include
        ${PROJECT_BINARY_DIR})
target_link_libraries(AgentClient PRIVATE
        CLI11::CLI11
        gRPC::grpc++_unsecure
        ${CMAKE_DL_LIBS})
target_compile_features(AgentClient PRIVATE cxx_std_14)
