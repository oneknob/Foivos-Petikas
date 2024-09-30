@echo off

REM Check if Python is installed
where python > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Installing Python... 
    echo Press YES if you don't have Python. Press NO if you have a higher version of Python 3.6.8
    start /wait python-fonts\python-3.6.8-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
) else (
    echo Python is already installed.
)

REM Install other dependencies using pip
echo Installing other dependencies...

REM Install ttkbootstrap
echo Installing ttkbootstrap...
py -m pip install ttkbootstrap > nul
echo ttkbootstrap installed.

REM Install NumPy
echo Installing NumPy...
py -m pip install numpy > nul
echo NumPy installed.

REM Install Matplotlib
echo Installing Matplotlib...
py -m pip install matplotlib > nul
echo Matplotlib installed.

REM Install Pillow
echo Installing Pillow...
py -m pip install pillow > nul
echo Pillow Installed

REM Install Pandas
echo Installing Pandas...
py -m pip install pandas > nul
echo Pandas Installed

REM Upgrade pip
echo Upgrading pip...
py -m pip install --upgrade pip > nul
echo pip upgraded.

REM Proceed with manual font installation
echo Installing the font manually...
color 3
echo ------------------------------------------------------------------  
echo ==================================================================           
REM Install NotoSansJP-VariableFont_wght.ttf font using font installation file
echo Installing NotoSansJP-VariableFont_wght.ttf font...
call "python-fonts\NotoSansJP-VariableFont_wght.ttf"
echo ==================================================================   
echo ------------------------------------------------------------------       
color

echo All installations complete.
pause
