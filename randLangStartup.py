import subprocess
import random

def changeLang(langList) :
    subprocess.run(["powershell.exe", f"Set-WinUserLanguageList -Force {langList}"])

def main() :
    randNum = random.randint(1, 2)

    if (randNum == 1):
        lList = '("es-MX", "en-US", "fr-FR")'
    elif (randNum == 2):
        lList = '("fr-FR", "en-US", "es-MX")'

    changeLang(lList)

if __name__ == "__main__":
    main()