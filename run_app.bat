@echo off
cd /d "%~dp0"

echo Checking for required dependencies...
pip install -r requirements.txt

echo Starting Streamlit app...
streamlit run app.py

echo.

pause