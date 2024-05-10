@echo off
REM Check for Python and exit if not found
python --version >nul 2>&1 || (
    echo Python is not installed. Please install Python first.
    exit /b
)

REM Create a virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate.bat

REM Install required packages
pip install -r requirements.txt

REM Run the Flask app
python app.py
