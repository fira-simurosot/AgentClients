cmake_minimum_required(VERSION 3.15)
project(AgentClient VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)

# Add command option parser
add_subdirectory(CLI11)

add_executable(AgentClient
        include/platform.h
        src/main.cpp)

target_include_directories(AgentClient PRIVATE include)
target_link_libraries(AgentClient PRIVATE CLI11::CLI11)
