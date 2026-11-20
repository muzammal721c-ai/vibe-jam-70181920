@echo off
title AskSE Help Desk Server - CodeQuest 2026
echo ========================================================
echo   AskSE - Department of Software Engineering Help Desk
echo   CodeQuest 2026 - The University of Lahore
echo ========================================================
echo.
echo Starting AskSE server on http://localhost:5000...
echo.

py -3.9 server.py
if %ERRORLEVEL% NEQ 0 (
    python server.py
)

pause
