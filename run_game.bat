@echo off
title XO Game Delight
echo Starting XO Game Delight...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

REM Check if the game file exists
if not exist "xo_game_tkinter.py" (
    echo Error: xo_game_tkinter.py not found
    echo Make sure you're running this from the correct directory
    pause
    exit /b 1
)

REM Run the game
echo Launching game...
python xo_game_tkinter.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Game ended with an error. Press any key to close.
    pause >nul
)