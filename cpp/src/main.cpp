#include <iostream>
#include <string>
#include <stdexcept>
#include <CLI/CLI.hpp>
#include "config.h"
#include "strategy_server.h"

int main(int argc, char **argv) {
    try {
        CLI::App app(PROJECT_DESCRIPTION);

        auto print_version = [](int64_t /*count*/) {
            std::cout << PROJECT_NAME << " " << PROJECT_VERSION << std::endl;
            std::cout << PROJECT_DESCRIPTION << std::endl;
            std::exit(0);
        };
        app.add_flag("-V, --version", print_version, "Print version information");

        std::string so_name;
        std::string port;
        app.add_option("-s, --strategy", so_name, "Specify the strategy shared object file")
                ->required()
                ->check(CLI::ExistingFile);
        app.add_option("-p, --port", port, "Specify the port number")
                ->default_val("50051");

        CLI11_PARSE(app, argc, argv)

        run_strategy_server("0.0.0.0:" + port, so_name);

    } catch (const std::invalid_argument &ex) {
        std::cerr << "Fatal error: invalid argument: " << ex.what() << std::endl;
    } catch (const std::system_error &ex) {
        std::cerr << "Fatal error: " << ex.what() << std::endl;
        auto code = ex.code().value();
        if (code != 0) {
            std::cerr << "Code: " << code << std::endl;
        }
    }
}
