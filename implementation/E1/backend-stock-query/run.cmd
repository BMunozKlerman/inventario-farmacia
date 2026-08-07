@echo off
docker build -t e1-backend-stock-query "%~dp0."
if errorlevel 1 exit /b %errorlevel%
if /I "%~1"=="--build-only" exit /b 0
docker run --rm -p 8080:8080 -e POS_BEARER_TOKEN=local-demo-token e1-backend-stock-query
