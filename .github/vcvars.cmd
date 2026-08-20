@echo off
rem Locate the installed Visual Studio and enter its x64 build environment.
for /f "usebackq tokens=*" %%i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -latest -property installationPath`) do set VSPATH=%%i
if "%VSPATH%"=="" (
    echo vswhere could not locate a Visual Studio installation
    exit /b 1
)
call "%VSPATH%\VC\Auxiliary\Build\vcvars64.bat"
