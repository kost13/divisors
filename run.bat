@echo off

SETLOCAL

if not exist .\bin\divisors.pyd (
    call build_cpp.bat
)

start "" http://127.0.0.1:8000/

python manage.py runserver

ENDLOCAL



