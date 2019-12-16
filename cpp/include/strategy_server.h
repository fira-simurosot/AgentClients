#pragma once

#include <string>
#include <REF2CLI/service.grpc.pb.h>
#include "cpp_strategy.h"

class StrategyServer final : public fira_message::ref_to_cli::Referee::Service {
    grpc::Status Register(grpc::ServerContext *context,
                          const fira_message::ref_to_cli::TeamInfo *request,
                          fira_message::ref_to_cli::TeamName *response) override;

    grpc::Status RunStrategy(grpc::ServerContext *context,
                             const fira_message::ref_to_cli::Environment *request,
                             fira_message::ref_to_cli::Command *response) override;

    grpc::Status SetBall(grpc::ServerContext *context,
                         const fira_message::ref_to_cli::Environment *request,
                         fira_message::Ball *response) override;

    grpc::Status SetFormerRobots(grpc::ServerContext *context,
                                 const fira_message::ref_to_cli::Environment *request,
                                 fira_message::ref_to_cli::Robots *response) override;

    grpc::Status SetLaterRobots(grpc::ServerContext *context,
                                const fira_message::ref_to_cli::Environment *request,
                                fira_message::ref_to_cli::Robots *response) override;

    /// Call the C++ strategy's <code>OnEvent</code> method when the phase has changed,
    /// and update current phase.
    /// @param phase Phase in this frame
    void notify_phase_change(const fira_message::ref_to_cli::FoulInfo_PhaseType& phase);

    void notify_judge_result(const fira_message::ref_to_cli::FoulInfo &foul_info);

    fira_message::ref_to_cli::FoulInfo_PhaseType current_phase;
    fira_message::ref_to_cli::Color self_color;
    cpp_interface::Ball ball_set;
    CppStrategy cpp_strategy;

public:
    explicit StrategyServer(const std::string_view so_name);
};

void run_strategy_server(const std::string &addr, const std::string &so_name);
