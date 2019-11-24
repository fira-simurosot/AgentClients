#pragma once

#include <string>
#include <memory>

#ifdef __linux__
    #include <dlfcn.h>
#endif
#ifdef _WIN32
#endif

#include "platform.h"

class CppStrategy {
    // use std::unique_ptr to store handle in order to make CppStrategy move-only
#ifdef __linux__
    static constexpr auto close_fn = [](void *handle) { dlclose(handle); };
#endif
#ifdef _WIN32
    static constexpr auto close_fn = [](void *handle) { };
#endif
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

