# - Find WS2_32
# This will define the following variables
#
#    WS2_32_FOUND        - True if WS2_32 found.
#
# and the following imported targets
#
#    WS2_32::WS2_32
#

find_library(WS2_32_LIBRARY WS2_32)
mark_as_advanced(WS2_32_LIBRARY)

# handle the QUIETLY and REQUIRED arguments and set WS2_32_FOUND to TRUE if
# all listed variables are TRUE
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(WS2_32
    REQUIRED_VARS WS2_32_LIBRARY)

if(WS2_32_FOUND AND NOT TARGET WS2_32::WS2_32)
    add_library(WS2_32::WS2_32 STATIC IMPORTED)
    set_target_properties(WS2_32::WS2_32 PROPERTIES
        IMPORTED_LOCATION "${WS2_32_LIBRARY}"
    )
endif()

