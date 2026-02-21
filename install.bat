@echo off

SETLOCAL ENABLEDELAYEDEXPANSION

echo Installing pnpm
call npm i -g pnpm
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install pnpm.
    pause
    exit /b %ERRORLEVEL%
)

echo Installing Typescript dependencies
call pnpm install 
IF %ERRORLEVEL% NEQ 0 (
    echo pnpm install failed.
    pause
    exit /b %ERRORLEVEL%
)

echo Compiling project
call tsc
IF %ERRORLEVEL% NEQ 0 (
    echo TypeScript compilation failed.
    pause
    exit /b %ERRORLEVEL%
)

echo Installing Python dependencies
python -m pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo Python requirements installation failed.
    pause
    exit /b %ERRORLEVEL%
)

echo Everything has been installed!
pause
