@echo off
cd resources
call "%~dp0pyenv\Scripts\activate_fix.bat"
python fix_exe.py fix "%~dp0pyenv\Scripts\uvicorn.exe"
rem lo de abajo necesita permiso de administrador
rem netsh advfirewall firewall add rule name="uvicorn" program="%~dp0pyenv\Scripts\uvicorn.exe" protocol=tcp dir=in enable=yes action=allow profile=Private
uvicorn pysrc.api:app