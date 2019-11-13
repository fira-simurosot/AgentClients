#pragma once

#include <string>
#include "platform.h"

class CppStrategy {
    void *handle;

    using OnEvent = void (*)(cpp_interface::EventType type, void *argument);
    using GetTeamInfo = void (*)(cpp_interface::TeamInfo *teamInfo);
    using GetInstruction = void (*)(cpp_interface::Field *field);
    using GetPlacement = void (*)(cpp_interface::Field *field);

public:
    explicit CppStrategy(const std::string& so_name);
    CppStrategy(const CppStrategy&) = delete;
    CppStrategy& operator=(const CppStrategy&) = delete;
    // the following two are not necessarily deleted, but should have a custom implementation
    CppStrategy(CppStrategy&&) = delete;
    CppStrategy& operator=(CppStrategy&&) = delete;
    ~CppStrategy();

    OnEvent on_event;
    GetInstruction get_instruction;
    GetPlacement get_placement;
    GetTeamInfo get_team_info;
};

