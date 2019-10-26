#include <iostream>
#include "CLI/CLI.hpp"
#include "config.h"

int main(int argc, char **argv) {
    CLI::App app(PROJECT_DESCRIPTION);

    auto print_version = [](int64_t count) {
        std::cout << PROJECT_NAME << " " << PROJECT_VERSION << std::endl;
        std::cout << PROJECT_DESCRIPTION << std::endl;
        std::exit(0);
    };
    app.add_flag("-V, --version", print_version, "Prints version information");

    CLI11_PARSE(app, argc, argv);
}