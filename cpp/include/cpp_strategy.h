#pragma once

#include <string>
#include <memory>

#include "platform.h"

class CppStrategy {
    // use std::unique_ptr to store handle in order to make CppStrategy move-only
    static void close_fn(void *handle);
    std::unique_ptr<void, decltype(&close_fn)> handle = {nullptr, close_fn};

    using OnEvent = void (*)(cpp_interface::EventType type, void *argument);
    using GetTeamInfo = void (*)(cpp_interface::TeamInfo *teamInfo);
    using GetInstruction = void (*)(cpp_interface::Field *field);
    using GetPlacement = void (*)(cpp_interface::Field *field);

public:
    explicit CppStrategy(const std::string& so_name);

    OnEvent on_event;
    GetInstruction get_instruction;
    GetPlacement get_placement;
    GetTeamInfo get_team_info;
};

