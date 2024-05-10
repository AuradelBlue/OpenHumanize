@echo off
setlocal EnableDelayedExpansion

echo Verifying Python virtual environment...
if not exist ".\env\Scripts\python.exe" (
    echo Virtual environment not found. Creating one...
    python -m venv env
    if errorlevel 1 (
        echo Failed to create virtual environment.
        exit /b 1
    )
)
echo Activating virtual environment...
call .\env\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate the virtual environment.
    exit /b 1
)

echo Installing required packages from requirements.txt...
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo Failed to install required packages.
    exit /b 1
)

echo Starting the Flask application...
python app.py
if errorlevel 1 (
    echo Flask application terminated with errors.
    exit /b 1
)

endlocal
