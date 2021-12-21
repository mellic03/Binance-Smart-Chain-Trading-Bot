@echo off

echo A few dependencies have to be met in order for the bot to work, this setup file exists to make getting those dependencies easier
pause

echo.
echo First, python has to be installed, make sure to so select "custom install" and check all optional boxes during the installation
pause
echo Running python installer
echo.
echo Come back to this window after python has finished installing
echo.

reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT

if %OS%==32BIT dependencies\python-3.10.1.exe
if %OS%==64BIT dependencies\python-3.10.1-amd64.exe


echo Next you need to install visual c++ build tools, check the box for "desktop development with c++" and install
pause

dependencies\vs_buildtools.exe

echo Come back to this window after build tools have finished installing
pause
echo.

echo Continue to install python libraries
pause
pip3 install -r dependencies\requirements.txt
echo Ignore aprturl error if you have one

echo.
echo.

echo Finished!
pause
exit