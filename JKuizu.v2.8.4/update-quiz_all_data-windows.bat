@echo off
setlocal

rem Set the URL of the file to be downloaded
set "file_url=https://docs.google.com/spreadsheets/d/1gd39s6qk4QlvLr-mlJgii67-tbycbQ4m/export?format=csv"

rem Set the name of the file to be saved
set "downloaded_file=quiz_all_data.csv"

rem Download the file
powershell -Command "(New-Object Net.WebClient).DownloadFile('%file_url%', '%downloaded_file%')"

rem Replace the existing file with the downloaded one, if it exists
if exist "%downloaded_file%" (
    copy /Y "%downloaded_file%" "%~dp0\%downloaded_file%"
    echo File download and replacement complete.
) else (
    echo Failed to download the file.
)
pause