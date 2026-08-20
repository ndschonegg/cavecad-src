cmake_minimum_required(VERSION 3.16)

include(../../CMakeInclude.txt)

project(cavecadcustomwidgets VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(${QT_VER} REQUIRED COMPONENTS Core Widgets Concurrent Gui Network OpenGL Sql Svg Xml PrintSupport Qml)
qt_standard_project_setup()

if(WIN32)
    set(RC customwidgets.rc)
endif()

if (CMAKE_BUILD_TYPE STREQUAL "Release")
    link_directories(${CMAKE_CURRENT_SOURCE_DIR}/../../release)
else()
    link_directories(${CMAKE_CURRENT_SOURCE_DIR}/../../debug)
endif()

add_library(cavecadcustomwidgets SHARED
    RCharacterWidgetPlugin.cpp RCharacterWidgetPlugin.h
    RColorComboPlugin.cpp RColorComboPlugin.h
    RComboBoxPlugin.cpp RComboBoxPlugin.h
    RCommandLinePlugin.cpp RCommandLinePlugin.h
    RCustomWidgets.cpp RCustomWidgets.h
    RFontChooserWidgetPlugin.cpp RFontChooserWidgetPlugin.h
    RGraphicsViewQtPlugin.cpp RGraphicsViewQtPlugin.h
    RLinetypeComboPlugin.cpp RLinetypeComboPlugin.h
    RLineweightComboPlugin.cpp RLineweightComboPlugin.h
    RListViewPlugin.cpp RListViewPlugin.h
    RMathComboBoxPlugin.cpp RMathComboBoxPlugin.h
    RMathLineEditPlugin.cpp RMathLineEditPlugin.h
    RMdiChildQtPlugin.cpp RMdiChildQtPlugin.h
    RRulerQtPlugin.cpp RRulerQtPlugin.h
    RShortcutLineEditPlugin.cpp RShortcutLineEditPlugin.h
    RTextEditPlugin.cpp RTextEditPlugin.h
    ${RC}
)
target_include_directories(cavecadcustomwidgets PRIVATE
    ../../src/core
    ../../src/core/math
    ../../src/entity
    ../../src/gui
)

target_compile_definitions(cavecadcustomwidgets PRIVATE
    QCAD_DLL
)

set_target_properties(cavecadcustomwidgets PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../../plugins/designer)
set_target_properties(cavecadcustomwidgets PROPERTIES RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/../../plugins/designer)

target_link_libraries(cavecadcustomwidgets PRIVATE
    # Remove: L${CMAKE_CURRENT_SOURCE_DIR}/
    Qt::Core
    Qt::Gui
    Qt::Widgets
    Qt::Network
    Qt::OpenGL
    Qt::Sql
    Qt::Svg
    Qt::Xml
    cavecadcore
    cavecadgui
)
