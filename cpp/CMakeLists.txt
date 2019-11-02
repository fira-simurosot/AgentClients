cmake_minimum_required(VERSION 3.15)
project(AgentClient
        VERSION 0.1.0
        DESCRIPTION "FIRASIM C++ Agent Client"
        LANGUAGES CXX)

# Add command option parser
add_subdirectory(CLI11)

# Generate config file
configure_file(
        include/config.h.in
        ${PROJECT_BINARY_DIR}/config.h)

add_executable(AgentClient
        config.h
        include/platform.h
        src/main.cpp src/cpp_strategy.cpp include/cpp_strategy.h)

target_include_directories(AgentClient PRIVATE
        include
        ${PROJECT_BINARY_DIR})
target_link_libraries(AgentClient PRIVATE CLI11::CLI11 ${CMAKE_DL_LIBS})
target_compile_features(AgentClient PRIVATE cxx_std_14)
