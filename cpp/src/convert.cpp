#include <stdexcept>
#include <algorithm>
#include "convert.h"

using google::protobuf::RepeatedFieldBackInserter;
using google::protobuf::RepeatedPtrField;

cpp_interface::EventType to_cpp_interface(fira_message::ref_to_cli::FoulInfo_PhaseType phase) {
    switch (phase) {
        case fira_message::ref_to_cli::FoulInfo_PhaseType_FirstHalf:
            return cpp_interface::EventType::FirstHalfStart;

        case fira_message::ref_to_cli::FoulInfo_PhaseType_SecondHalf:
            return cpp_interface::EventType::SecondHalfStart;

        case fira_message::ref_to_cli::FoulInfo_PhaseType_Overtime:
            return cpp_interface::EventType::OvertimeStart;

        case fira_message::ref_to_cli::FoulInfo_PhaseType_PenaltyShootout:
            return cpp_interface::EventType::PenaltyShootoutStart;

        default:
            throw std::invalid_argument("phase");
    }
}

cpp_interface::JudgeType to_cpp_interface(fira_message::ref_to_cli::FoulInfo_FoulType foul_type) {
    switch (foul_type) {
        case fira_message::ref_to_cli::FoulInfo_FoulType_FreeBallLeftTop:
            return cpp_interface::JudgeType::FreeKickLeftTop;

        case fira_message::ref_to_cli::FoulInfo_FoulType_FreeBallRightTop:
            return cpp_interface::JudgeType::FreeKickRightTop;

        case fira_message::ref_to_cli::FoulInfo_FoulType_FreeBallLeftBot:
            return cpp_interface::JudgeType::FreeKickLeftBot;

        case fira_message::ref_to_cli::FoulInfo_FoulType_FreeBallRightBot:
            return cpp_interface::JudgeType::FreeKickRightBot;

        case fira_message::ref_to_cli::FoulInfo_FoulType_PlaceKick:
            return cpp_interface::JudgeType::PlaceKick;

        case fira_message::ref_to_cli::FoulInfo_FoulType_PenaltyKick:
            return cpp_interface::JudgeType::PenaltyKick;

        case fira_message::ref_to_cli::FoulInfo_FoulType_GoalKick:
            return cpp_interface::JudgeType::GoalKick;

        default:
            throw std::invalid_argument("foul_type");
    }
}

cpp_interface::Team to_cpp_interface(fira_message::ref_to_cli::Side side) {
    switch (side) {
        case fira_message::ref_to_cli::Self:
            return cpp_interface::Team::Self;
        case fira_message::ref_to_cli::Opponent:
            return cpp_interface::Team::Opponent;
        default:
            throw std::invalid_argument("side");
    }
}

cpp_interface::JudgeResultEvent to_cpp_interface(const fira_message::ref_to_cli::FoulInfo& foul_info) {
    return {
            .type = to_cpp_interface(foul_info.type()),
            .actor = to_cpp_interface(foul_info.actor()),
            .reason = {0},
    };
}

cpp_interface::Robot to_cpp_interface(const fira_message::Robot &robot) {
    return {
        .position = {
                .x = static_cast<float>(robot.x()),
                .y = static_cast<float>(robot.y()),
        },
        .rotation = static_cast<float>(robot.orientation()),
    };
}

static void transform_robots(cpp_interface::Robot target[],
                             const RepeatedPtrField<fira_message::Robot> &source) {
    std::vector<fira_message::Robot> self_robot_vec;
    std::copy(source.begin(), source.end(), self_robot_vec.begin());
    std::sort(self_robot_vec.begin(), self_robot_vec.end(),
              [](const fira_message::Robot &rhs, const fira_message::Robot &lhs) {
                  return rhs.robot_id() < lhs.robot_id();
              });
    std::transform(self_robot_vec.begin(), self_robot_vec.end(), target,
                   [](const fira_message::Robot &robot) { return to_cpp_interface(robot); });
}

cpp_interface::Field
to_cpp_interface(const fira_message::Frame &frame,
                 fira_message::ref_to_cli::Color self_color) {
    cpp_interface::Field field {
        .selfRobots = {},
        .opponentRobots = {},
        .ball = {
                .position = {
                        .x = static_cast<float>(frame.ball().x()),
                        .y = static_cast<float>(frame.ball().y()),
                }
        },
        .tick = 0
    };

    switch (self_color) {
        case fira_message::ref_to_cli::Y:
            transform_robots(field.selfRobots, frame.robots_yellow());
            transform_robots(field.opponentRobots, frame.robots_blue());
            break;
        case fira_message::ref_to_cli::B:
            transform_robots(field.selfRobots, frame.robots_blue());
            transform_robots(field.opponentRobots, frame.robots_yellow());
            break;
        default:
            break;
    }

    return field;
}

fira_message::ref_to_cli::Command from_cpp_interface(const cpp_interface::Field &field) {
    fira_message::ref_to_cli::Command command;
    constexpr int player_num = cpp_interface::PLAYERS_PER_SIDE;
    for (int i = 0; i < player_num; i++) {
        fira_message::ref_to_cli::WheelSpeed wheel_speed;
        wheel_speed.set_robot_id(i);
        wheel_speed.set_left(field.selfRobots[i].wheel.leftSpeed);
        wheel_speed.set_right(field.selfRobots[i].wheel.rightSpeed);
        *command.add_wheels() = std::move(wheel_speed);
    }
    return command;
}



