@echo off

REM When a python script (*.py) encounters an error, the terminal window abruptly closes.
REM Running the script from a parent window allows to keep the window open and see the error.

setlocal ENABLEDELAYEDEXPANSION

set "filename=%~n0"
set "filename=!filename:.debug=!"
set "python_file=%filename%.py"

python "%~dp0%python_file%" %*

IF %ERRORLEVEL% NEQ 0 (
    ECHO.
    ECHO Press any key to exit ...
    >nul TIMEOUT /T -1
)

