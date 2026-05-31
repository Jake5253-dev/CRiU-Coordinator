import typer
import os
import platform
import subprocess
import re
app = typer.Typer()


@app.command()
def main(name: str):
	print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbyae Ms. {name}. Have a good day.")
    
    else:
        print(f"Bye {name}!")

@app.command()
def env_hello():
    name = os.getenv("MY_NAME", "World")
    print(f"Hello {name} from Python")

@app.command()    
def printDirectory(function: bool = False):
    name = os.listdir()
    print("Here is a list of all files")
    for file in name:
        print(str(file)+ "\n")

def get_current_processes():
    """ Only works on Linux, do not use on windows"""

    systemString = platform.system()
    if systemString != "Linux":
        print("This is not a Linux system, not performing function")
    else:
        pid_list = subprocess.run(["ps"], capture_output=True, text=True)

        with open("pid_list_file.txt", "w") as f:
            f.write(pid_list.stdout)
        python_process_list = []
        with open("pid_list_file.txt", "r") as fexplorer:
            for line in fexplorer:
                # print(line.strip())
                if re.search("python|python3", line.strip()):
                    python_process_list.append(str(line.strip()))

        my_id = os.getpid()
        return python_process_list

@app.command()
def CRiU_Coordinator():
    print("Starting CRiU_Coordinator")
    who_am_i()
    process_list = get_current_processes()
    print("Ending CRiU_Coordinator")

@app.command()
def print_processes():
    who_am_i()
    print(get_current_processes())

def who_am_i():
    print(f"This process ID is {os.getpid()}")

if __name__ == "__main__":
    app()
