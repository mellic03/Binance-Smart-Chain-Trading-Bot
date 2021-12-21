@echo off

pip install -r dependencies\requirements.txt

echo Ignore aprturl error if you have one
echo.

echo.

echo Next you need to install visual c++ build tools, that will open now.
pause

dependencies\vs_buildtools.exe

echo.
echo Finished!
pause
exit