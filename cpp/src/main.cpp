#include "CLI/CLI.hpp"

int main(int argc, char **argv) {
    CLI::App app("FIRASIM C++ Agent Client");

    CLI11_PARSE(app, argc, argv);
}