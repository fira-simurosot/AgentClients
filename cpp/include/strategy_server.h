#pragma once

#include <string>
#include <REF2CLI/service.grpc.pb.h>

class StrategyServer final : public fira_message::ref_to_cli::Referee::Service {
    grpc::Status RunStrategy(grpc::ServerContext *context,
                             const fira_message::ref_to_cli::Environment *request,
                             fira_message::ref_to_cli::Command *response) override;
};

void run_strategy_server(const std::string &addr);
