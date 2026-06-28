"""Starting point for CRiU-Coordinator"""

from Process_Finder import Process_Finder

def print_logo():
    print(r"  ___ ___ _ _   _    ___ ___   ___   ")
    print(r" / __| _ (_) | | |  / __/ _ \ / _ \  ")
    print(r"| (__|   / | |_| | | (_| (_) | (_) | ")
    print(r" \___|_|_\_|\___/   \___\___/_\___/_ ")
    print(r"| _ \   \_ _| \| | /_\_   _/ _ \| _ \\")
    print(r"|   / |) | || .` |/ _ \| || (_) |   /")
    print(r"|_|_\___/___|_|\_/_/ \_\_| \___/|_|_\\")

def first_instructions():
    print("Welcome to CRiU Coordinator")
    print("Here are a list of processes on this VM")

if __name__ == "__main__":
    print_logo()
    first_instructions()
    pf = ProcessFinder()
    pf.get_process_list()