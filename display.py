from os import system, name
#import os
#use this if only import os:
#os.name, os.system('cls'), os.name

def print_menu():
    """Used to print out the menu options
    """
    print("-" * 20)
    print("** Audio Mgr 3000 **")
    print("-" * 20)
    print("[1] Register a new Album")
    print("[2] Register a new Song")
    print("[3] Display album catalog".title())
    print("[4] Print the songs inside the Album")
    print("[5] Count all the songs in the system")
    print("[6] Print all")
    print("[7] Total cost in catalog")
    print("[8] Most expensive album")
    print("[10] Change the title of an specific album")
    print("[11] Change the title of a specific song")
    print("[q] Quit")

def print_header(text):
    clear()
    print("-" * 30)
    print(text)
    print("-" * 30)

def clear():
    # if name in ('nt','dos'):#dos is for computers in the 1990s
        # return system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    # else:
        # _ = system('clear')

    return system('cls' if name=='nt' else 'clear')