#pragma once

#include <string>
#include "platform.h"

class cpp_strategy {
    void *handle;

    using OnEvent = void (*)(cpp_interface::EventType type, void *argument);
    using GetTeamInfo = void (*)(cpp_interface::TeamInfo *teamInfo);
    using GetInstruction = void (*)(cpp_interface::Field *field);
    using GetPlacement = void (*)(cpp_interface::Field *field);

public:
    explicit cpp_strategy(const std::string& so_name);
    ~cpp_strategy();

    OnEvent on_event;
    GetInstruction get_instruction;
    GetPlacement get_placement;
    GetTeamInfo get_team_info;
};

