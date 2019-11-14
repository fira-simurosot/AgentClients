#include "cpp_strategy.h"
#include <dlfcn.h>
#include <string>
#include <system_error>

template <typename T>
static T dlsym_wrapper(void *handle, const char *name) {
    dlerror();
    auto sym = (T) dlsym(handle, name);
    const char * dlsym_error = dlerror();
    if (dlsym_error) {
        throw std::system_error(std::error_code(), dlsym_error);
    }
    return sym;
}

CppStrategy::CppStrategy(const std::string& so_name)
        : handle(dlopen(so_name.c_str(), RTLD_LAZY), close_fn) {

    if (!handle) {
        throw std::system_error(std::error_code(), dlerror());
    }

    on_event = dlsym_wrapper<OnEvent>(handle.get(), "OnEvent");
    get_instruction = dlsym_wrapper<GetInstruction>(handle.get(), "GetInstruction");
    get_placement = dlsym_wrapper<GetPlacement>(handle.get(), "GetPlacement");
    get_team_info = dlsym_wrapper<GetTeamInfo>(handle.get(), "GetTeamInfo");
}

