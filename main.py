import install
import save
from colorama import Fore

# Prompt user what to do
def prompt():
    do = input(Fore.RESET + "What would you like to do today?\nS = Save, I = Install, Q = Quit\n")
    if do not in ["S", "I", "Q"]:
        print(Fore.RED + "You have entered an invalid option. Please try again...")
        prompt()
    elif do == "Q":
        print(Fore.RED + "Quitting...")
        exit()
    elif do == "S":
        save.run()
    elif do == "I":
        install.install()


if __name__ == '__main__':
    prompt()
