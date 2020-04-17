# C++ Agent Client

## Supported build tools

Tested with CMake 3.10 with following compilers:

- GCC 7.4.0 (provided by Ubuntu 18.04 LTS)
- Clang 7.0.0


## Installation

### Clone Sub Modules
```bash
git submodule update --recursive --init 
```

### Installation of GRPC 

#### Ubuntu
```bash
sudo add-apt-repository ppa:webispy/grpc
sudo apt-get update
sudo apt install -y libgrpc++-dev libprotobuf-dev protobuf-compiler-grpc clang-7
```

#### Arch Linux
```bash
pacman -S grpc
```
