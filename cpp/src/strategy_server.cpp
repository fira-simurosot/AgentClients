#include <memory>
#include <grpcpp/grpcpp.h>
#include "convert.h"
#include "strategy_server.h"

using fira_message::ref_to_cli::Environment;
using fira_message::ref_to_cli::Command;
using fira_message::ref_to_cli::Robots;
using fira_message::ref_to_cli::FoulInfo;
using fira_message::ref_to_cli::FoulInfo_PhaseType;
using fira_message::Ball;

grpc::Status
StrategyServer::Register(grpc::ServerContext *context,
                         const fira_message::ref_to_cli::TeamInfo *request,
                         fira_message::ref_to_cli::TeamName *response) {
    self_color = request->color();

    cpp_interface::TeamInfo team_info{};
    cpp_strategy.get_team_info(&team_info);
    response->set_name(team_info.teamName);

    return grpc::Status::OK;
}

grpc::Status
StrategyServer::RunStrategy(grpc::ServerContext *context,
                            const Environment *request,
                            Command *response) {
    const auto& frame = request->frame();
    auto field = to_cpp_interface(frame, self_color);
    cpp_strategy.get_instruction(&field);
    *response = from_cpp_interface(field);
    return grpc::Status::OK;
}

grpc::Status
StrategyServer::SetBall(grpc::ServerContext *context,
                        const Environment *request,
                        Ball *response) {
    return grpc::Status::OK;
}

grpc::Status
StrategyServer::SetFormerRobots(grpc::ServerContext *context,
                                const Environment *request,
                                Robots *response) {
    const auto &foul_info = request->foulinfo();
    notify_phase_change(foul_info.phase());
    notify_judge_result(foul_info);
    return grpc::Status::OK;
}

grpc::Status
StrategyServer::SetLaterRobots(grpc::ServerContext *context,
                               const Environment *request,
                               Robots *response) {
    const auto &foul_info = request->foulinfo();
    notify_phase_change(foul_info.phase());
    notify_judge_result(foul_info);
    return grpc::Status::OK;
}

StrategyServer::StrategyServer(const std::string &so_name)
        : current_phase(FoulInfo_PhaseType::FoulInfo_PhaseType_Stopped),
          cpp_strategy(so_name) {
}

void StrategyServer::notify_phase_change(const FoulInfo_PhaseType& phase) {
    if (phase != current_phase) {
        cpp_strategy.on_event(to_cpp_interface(phase), nullptr);
        current_phase = phase;
    }
}

void StrategyServer::notify_judge_result(const FoulInfo &foul_info) {
    cpp_interface::JudgeResultEvent event = to_cpp_interface(foul_info);
    cpp_strategy.on_event(cpp_interface::EventType::JudgeResult, static_cast<void*>(&event));
}

void run_strategy_server(const std::string &addr, const std::string &so_name) {
    StrategyServer service(so_name);

    grpc::ServerBuilder builder;
    builder.AddListeningPort(addr, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);
    std::unique_ptr server(builder.BuildAndStart());
    std::cout << "Server listening on " << addr << std::endl;

    server->Wait();
}
