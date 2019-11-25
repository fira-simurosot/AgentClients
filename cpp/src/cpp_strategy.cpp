#include "cpp_strategy.h"
#include <string>
#include <system_error>

#ifdef __linux__
#include <dlfcn.h>

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
#endif

#ifdef _WIN32
#include <Windows.h>

template <typename T>
static T dlsym_wrapper(void *handle, const char *name) {
    auto sym = (T) GetProcAddress(static_cast<HINSTANCE>(handle), name);
    if (!sym) {
        throw std::system_error(GetLastError(), std::system_category(), "Error loading function");
    }
    return sym;
}

CppStrategy::CppStrategy(const std::string& so_name)
        : handle(LoadLibrary(so_name.c_str()), close_fn) {
    if (!handle) {
        throw std::system_error(GetLastError(), std::system_category(), "Error loading library");
    }

    on_event = dlsym_wrapper<OnEvent>(handle.get(), "OnEvent");
    get_instruction = dlsym_wrapper<GetInstruction>(handle.get(), "GetInstruction");
    get_placement = dlsym_wrapper<GetPlacement>(handle.get(), "GetPlacement");
    get_team_info = dlsym_wrapper<GetTeamInfo>(handle.get(), "GetTeamInfo");
}
#endif
