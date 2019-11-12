#include "cpp_strategy.h"
#include "platform.h"
#include <dlfcn.h>
#include <string>
#include <functional>
#include <system_error>

template <typename T>
T dlsym_wrapper(void *handle, const char *name) {
    dlerror();
    auto sym = (T) dlsym(handle, name);
    const char * dlsym_error = dlerror();
    if (dlsym_error) {
        throw std::system_error(std::error_code(), dlsym_error);
    }
    return sym;
}

CppStrategy::CppStrategy(const std::string& so_name) {
    handle = dlopen(so_name.c_str(), RTLD_LAZY);

    if (!handle) {
        throw std::system_error(std::error_code(), dlerror());
    }

    on_event = dlsym_wrapper<OnEvent>(handle, "OnEvent");
    get_instruction = dlsym_wrapper<GetInstruction>(handle, "GetInstruction");
    get_placement = dlsym_wrapper<GetPlacement>(handle, "GetPlacement");
    get_team_info = dlsym_wrapper<GetTeamInfo>(handle, "GetTeamInfo");
}

CppStrategy::~CppStrategy() {
    dlclose(handle);
}
