from colorama import Fore
import pickle
import os
from pathlib import Path


class Backup:
    def __init__(self):
        if not os.path.exists('.storage/'):
            os.makedirs('.storage/')
        Path('.storage/var_storage.pk').touch(exist_ok=True)
        self.varStorage = ".storage/var_storage.pk"
        # Get preferred file save location, set to default if none
        try:
            self.saveLocation = pickle.load(open(self.varStorage, "rb"))
        except EOFError:
            self.saveLocation = ".storage/"
        self.fileLocation = self.saveLocation + "brew-list.txt"
        self.prompt()

    # Prompt user to select an option
    def prompt(self):
        do = input(
            Fore.RESET + "What would you like to do today?\n=================================\nS = Save package list\nI = Install packages from list\nM = Modify Save Location\nQ = Quit program\n=================================\n")
        if do not in ["S", "I", "M", "Q"]:
            print(Fore.RED + "You have entered an invalid option. Please try again...")
            Backup.prompt(self)
        elif do == "Q":
            print(Fore.RED + "Quitting...")
            exit()
        elif do == "M":
            Backup.modify(self)
        elif do == "S":
            Backup.save(self)
        elif do == "I":
            Backup.install(self)
        return self.saveLocation, self.fileLocation

    # Modify the save location and store it for future program use
    def modify(self):
        self.saveLocation = input(
            "\nEnter a valid save path (default: .storage/):\n" + "Current save location is: " + self.saveLocation + "\n")
        with open(self.varStorage, "wb") as file:
            pickle.dump(self.saveLocation, file)
        self.fileLocation = self.saveLocation + "brew-list.txt"
        Backup.prompt(self)

    # Create required directories and files if needed
    def initialize(self):
        if not os.path.exists(self.saveLocation):
            os.makedirs(self.saveLocation)

    # Save list of installed packages in homebrew
    def saveBrewInstallFile(self):
        os.system("brew leaves > " + self.fileLocation)
        print(Fore.GREEN + "Package list saved!\n")
        Backup.prompt(self)

    def save(self):
        Backup.initialize(self)
        Backup.saveBrewInstallFile(self)

    # Install programs from saved list
    def install(self):
        installList = open(self.fileLocation, "r").read().replace("\n", " ")
        os.system("brew install " + installList)
        print(Fore.GREEN + "Install complete!\n")
        Backup.prompt(self)


if __name__ == '__main__':
    Backup()
