include( ../run/run.pri )

CONFIG += console
TARGET = cavecadcmd.com

QMAKE_POST_LINK = mv "$${DESTDIR}/cavecadcmd.com.exe" "$${DESTDIR}/cavecadcmd.com"
