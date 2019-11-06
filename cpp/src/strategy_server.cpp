#include <memory>
#include <grpcpp/grpcpp.h>
#include "strategy_server.h"

grpc::Status
StrategyServer::RunStrategy(
        grpc::ServerContext *context,
        const fira_message::ref_to_cli::Environment *request,
        fira_message::ref_to_cli::Command *response) {
    return Service::RunStrategy(context, request, response);
}

void run_strategy_server(const std::string &addr) {
    StrategyServer service;

    grpc::ServerBuilder builder;
    builder.AddListeningPort(addr, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << addr << std::endl;

    server->Wait();
}
