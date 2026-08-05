@echo off
setlocal
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\run-project.ps1" %*
exit /b %ERRORLEVEL%
