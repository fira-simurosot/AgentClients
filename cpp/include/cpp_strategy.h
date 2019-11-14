#pragma once

#include <string>
#include <memory>
#include <dlfcn.h>
#include "platform.h"

class CppStrategy {
    // use std::unique_ptr to store handle in order to make CppStrategy move-only
    static constexpr auto close_fn = [](void *handle) { dlclose(handle); };
    std::unique_ptr<void, decltype(close_fn)> handle;

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

