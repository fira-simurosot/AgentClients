#include <iostream>
#include <string>
#include <CLI/CLI.hpp>
#include "config.h"
#include "strategy_server.h"

int main(int argc, char **argv) {
    CLI::App app(PROJECT_DESCRIPTION);

    auto print_version = [](int64_t count) {
        std::cout << PROJECT_NAME << " " << PROJECT_VERSION << std::endl;
        std::cout << PROJECT_DESCRIPTION << std::endl;
        std::exit(0);
    };
    app.add_flag("-V, --version", print_version, "Print version information");

    std::string so_name;
    app.add_option("-s, --strategy", so_name, "Specify the strategy shared object file")
            ->check(CLI::ExistingFile);

    CLI11_PARSE(app, argc, argv);

    run_strategy_server("0.0.0.0:50051", so_name);
}
