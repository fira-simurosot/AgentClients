#pragma once

#include "REF2CLI/messages.pb.h"
#include "platform.h"

cpp_interface::EventType to_cpp_interface(fira_message::ref_to_cli::FoulInfo_PhaseType phase);

cpp_interface::JudgeType to_cpp_interface(fira_message::ref_to_cli::FoulInfo_FoulType foul_type);

cpp_interface::Team to_cpp_interface(fira_message::ref_to_cli::Side side);

cpp_interface::JudgeResultEvent to_cpp_interface(const fira_message::ref_to_cli::FoulInfo& foul_info);

cpp_interface::Robot to_cpp_interface(const fira_message::Robot& robot);

cpp_interface::Field
to_cpp_interface(const fira_message::Frame &frame, fira_message::ref_to_cli::Color self_color);

fira_message::ref_to_cli::Command from_cpp_interface(const cpp_interface::Field &field);
