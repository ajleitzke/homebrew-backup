import os
import main
from colorama import Fore

# Send list of packages to homebrew to be installed
def install():
    installList = open("files/brew.txt", "r").read().replace("\n", " ")
    os.system("brew install " + installList)
    print(Fore.GREEN + "Install complete!")
    main.prompt()
