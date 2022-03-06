@echo off

echo Installing Spicetify...
powershell .\inst.ps1
echo DONE!
echo.
echo.
echo Installing Spicetify Marketplace...
powershell .\mrk.ps1
echo DONE!
echo.
echo.
echo Applying...!
start cmd /c "spicetify apply"
pause