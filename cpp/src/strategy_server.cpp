#include "strategy_server.h"
#include "convert.h"
#include <grpcpp/grpcpp.h>
#include <memory>

#if __has_include(<filesystem>)
#  include <filesystem>
namespace fs = std::filesystem;
#else
#  include <experimental/filesystem>
namespace fs = std::experimental::filesystem;
#endif

using fira_message::ref_to_cli::Environment;
using fira_message::ref_to_cli::Command;
using fira_message::ref_to_cli::Robots;
using fira_message::ref_to_cli::FoulInfo;
using fira_message::ref_to_cli::FoulInfo_PhaseType;
using fira_message::Ball;

grpc::Status
StrategyServer::Register(grpc::ServerContext* /*context*/,
                         const fira_message::ref_to_cli::TeamInfo *request,
                         fira_message::ref_to_cli::TeamName *response) {
    self_color = request->color();

    cpp_interface::TeamInfo team_info{};
    cpp_strategy.get_team_info(&team_info);
    response->set_name(static_cast<const char*>(team_info.teamName));

    return grpc::Status::OK;
}

grpc::Status
StrategyServer::RunStrategy(grpc::ServerContext* /*context*/,
                            const Environment *request,
                            Command *response) {
    const auto& frame = request->frame();
    auto field = to_cpp_interface(frame, self_color);
    cpp_strategy.get_instruction(&field);
    *response = convert_field_to_command(field);
    return grpc::Status::OK;
}

grpc::Status
StrategyServer::SetBall(grpc::ServerContext* /*context*/,
                        const Environment* /*request*/,
                        Ball *response) {
    response->set_x(ball_set.position.x);
    response->set_y(ball_set.position.y);
    return grpc::Status::OK;
}

grpc::Status
StrategyServer::SetFormerRobots(grpc::ServerContext* /*context*/,
                                const Environment *request,
                                Robots *response) {
    const auto &foul_info = request->foulinfo();
    notify_phase_change(foul_info.phase());
    notify_judge_result(foul_info);
    auto field = to_cpp_interface(request->frame(), self_color);
    cpp_strategy.get_placement(&field);
    *response = convert_field_to_robots(field);
    ball_set = field.ball;
    return grpc::Status::OK;
}

grpc::Status
StrategyServer::SetLaterRobots(grpc::ServerContext *context,
                               const Environment *request,
                               Robots *response) {
    // same as SetFormerRobots
    return SetFormerRobots(context, request, response);
}

StrategyServer::StrategyServer(const std::string_view so_name)
        : current_phase(FoulInfo_PhaseType::FoulInfo_PhaseType_Stopped),
          self_color(),
          ball_set(),
          cpp_strategy(fs::canonical(fs::path(so_name)).string()) {
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
