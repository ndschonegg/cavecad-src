include(../../CMakeInclude.txt)
project(cavecadcmd)
include(../run/CMakeInclude.txt)

set_target_properties(cavecadcmd PROPERTIES
    OUTPUT_NAME "cavecadcmd"
    SUFFIX ".com"
)

set_target_properties(cavecadcmd PROPERTIES
    WIN32_EXECUTABLE FALSE
    MACOSX_BUNDLE FALSE
)


#add_custom_command(TARGET cavecadcmd.com POST_BUILD
#    COMMAND ${CMAKE_COMMAND} -E rename
#        $<TARGET_FILE:cavecadcmd>
#        $<TARGET_FILE_DIR:cavecadcmd>/cavecadcmd.com
#    COMMENT "Renaming $<TARGET_FILE_NAME:cavecadcmd> to cavecadcmd.com"
#)
