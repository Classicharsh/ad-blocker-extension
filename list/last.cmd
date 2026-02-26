python clean_blocklist.py hosts.txt n.txt

python append_file.py n.txt blocklist.txt



@echo off
set FILE=blocklist.txt
set PARENT_DIR=%cd%\..

REM Copy and overwrite if file exists
copy /Y "%FILE%" "%PARENT_DIR%"

REM Move and overwrite if file exists
move /Y "%FILE%" "%PARENT_DIR%"

echo Done!
pause
