CONFIG      += plugin
TARGET      = example
include(../../../shared.pri)

TEMPLATE    = lib
HEADERS     = RExamplePlugin.h
SOURCES     = RExamplePlugin.cpp
DESTDIR     = $$PWD/../../../plugins
LIBS += -lcavecadcore -lcavecadgui -lcavecadecmaapi
RESOURCES   = scripts.qrc
