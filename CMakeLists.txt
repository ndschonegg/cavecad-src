cmake_minimum_required(VERSION 3.16)

include(CMakeInclude.txt)

project(cavecad VERSION 1.0 LANGUAGES CXX)

set(PROJECT_ROOT_DIR ${PROJECT_SOURCE_DIR})

# CaveCAD: the application's own version number, kept in one place (the
# VERSION file at the repository root) and handed to the code as a macro.
# It is CaveCAD's version, not the QCAD framework version in RVersion.h,
# which keeps tracking upstream.
file(STRINGS "${PROJECT_SOURCE_DIR}/VERSION" CAVECAD_VERSION LIMIT_COUNT 1)
string(STRIP "${CAVECAD_VERSION}" CAVECAD_VERSION)
add_compile_definitions(CAVECAD_VERSION_STRING="${CAVECAD_VERSION}")
message(STATUS "CaveCAD version: ${CAVECAD_VERSION}")

option(BUILD_QT6 "Building with Qt 6.x" ON)

add_subdirectory(src)
