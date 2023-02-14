import os
import subprocess
import main
from colorama import Fore


# Create required directories and files
def initialize():
    initializationTest = subprocess.run(["mkdir", "files"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if initializationTest.returncode != "1":
        os.system("touch files/brew.txt")


# Save list of installed packages in homebrew
def saveBrewInstallFile():
    os.system("brew leaves > files/brew.txt")
    print(Fore.GREEN + "Package list saved!")
    main.prompt()


def run():
    initialize()
    saveBrewInstallFile()