@echo off

cd /d "%~dp0.."

if not exist venv (
    echo venv file not found
)

if not exist generated (
    mkdir generated
)

if exist venv (
    REM 가상환경 활성화
    call venv\scripts\activate.bat

    python -m grpc_tools.protoc -Iproto --python_out=generated --grpc_python_out=generated proto\vision.proto

    REM 결과 확인
    if %errorlevel% neq 0 (
        echo [ERROR] proto generation failed
        exit /b %errorlevel%
    )

    echo [OK] proto files generated in /generated
)

