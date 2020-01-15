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

void CppStrategy::close_fn(void *handle) {
    dlclose(handle);
}

CppStrategy::CppStrategy(const std::string& so_name) {
    // if so_name is empty, will load this program itself
    if (so_name.empty()) {
        throw std::invalid_argument("name of so can't be empty");
    }

    handle.reset(dlopen(so_name.c_str(), RTLD_LAZY));

    if (!handle) {
        throw std::system_error(std::error_code(), dlerror());
    }

    on_event = dlsym_wrapper<OnEvent>(handle.get(), "OnEvent");
    get_instruction = dlsym_wrapper<GetInstruction>(handle.get(), "GetInstruction");
    get_placement = dlsym_wrapper<GetPlacement>(handle.get(), "GetPlacement");
    get_team_info = dlsym_wrapper<GetTeamInfo>(handle.get(), "GetTeamInfo");
}
#endif

#ifdef __APPLE__
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

void CppStrategy::close_fn(void *handle) {
    dlclose(handle);
}

CppStrategy::CppStrategy(const std::string& so_name) {
    // if so_name is empty, will load this program itself
    if (so_name.empty()) {
        throw std::invalid_argument("name of so can't be empty");
    }

    handle.reset(dlopen(so_name.c_str(), RTLD_LAZY));

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

void CppStrategy::close_fn(void *handle) {
    FreeLibrary(static_cast<HINSTANCE>(handle));
}

CppStrategy::CppStrategy(const std::string& so_name) {
    handle.reset(LoadLibrary(so_name.c_str()));

    if (!handle) {
        throw std::system_error(GetLastError(), std::system_category(), "Error loading library");
    }

    on_event = dlsym_wrapper<OnEvent>(handle.get(), "OnEvent");
    get_instruction = dlsym_wrapper<GetInstruction>(handle.get(), "GetInstruction");
    get_placement = dlsym_wrapper<GetPlacement>(handle.get(), "GetPlacement");
    get_team_info = dlsym_wrapper<GetTeamInfo>(handle.get(), "GetTeamInfo");
}
#endif
