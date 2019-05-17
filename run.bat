@echo off
call "%~dp0pyenv\Scripts\activate_fix.bat"
cd resources
uvicorn pysrc.api:app