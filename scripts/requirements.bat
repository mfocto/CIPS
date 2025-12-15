@echo off

REM bat 파일이 루트에서 실행되도록 설정
cd /d "%~dp0.."

if exist venv (
    REM 가상환경 활성화
    call venv\scripts\activate.bat

    REM 패키지 설치 목록
    REM grpcio
    REM grpcio-tools
    REM opencv-python

    pip install grpcio grpcio-tools opencv-python

    REM 완료 메시지 표시
    echo.
    echo ====== pip install complete! ======
)

if not exist venv (
    echo venv not found
)