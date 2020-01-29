# C++ Agent Client

## Supported build tools

Tested with CMake 3.10 with following compilers:

- GCC 7.4.0 (provided by Ubuntu 18.04 LTS)
- Clang 7.0.0
- MSVC latest (Visual Studio 2019)


## Installation of GRPC for Linux
```bash
sudo add-apt-repository ppa:webispy/grpc
sudo apt-get update
sudo apt install -y libgrpc++-dev libprotobuf-dev protobuf-compiler-grpc clang-7
```
