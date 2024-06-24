@echo off
REM Activate the virtual environment
cd C:\Users\sheha\Documents\Code\stock amrket\venv\Scripts
call activate

REM Run the ETL script
python C:\Users\sheha\Documents\Code\stock amrket\etl.py

REM Deactivate the virtual environment
deactivate
