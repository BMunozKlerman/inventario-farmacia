@echo off
python "%~dp0scripts\run_project.py" %*
exit /b %ERRORLEVEL%
