@echo off

echo A few dependencies have to be met in order for the bot to work, this setup file exists to make getting those dependencies easier
pause

echo First, python has to be installed, make sure to check all optional boxes during the installation
pause
echo Running python installer
echo Come back to this window after python has finished installing

reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT

if %OS%==32BIT dependencies\python-3.10.1.exe
if %OS%==64BIT dependencies\python-3.10.1-amd64.exe


echo Next you need to install visual c++ build tools, that will open now.
pause

dependencies\vs_buildtools.exe
echo.

echo Continue to install python libraries
pause
pip install -r dependencies\requirements.txt
echo Ignore aprturl error if you have one

echo.
echo.

echo Finished!
pause
exit