rem Keep powershell from opening a window on execution
@echo off

rem Runs my python language change automation script w/o opening powershell
start "" /B "C:\Users\adkin\anaconda3\pythonw.exe" "C:\Users\adkin\OneDrive\Documents\Work\PersonalProjects\StartupAuto\randLangStartup.py"

rem Opens ChatGPT at startup to always have my Jarvis
start "" "https://chatgpt.com/"