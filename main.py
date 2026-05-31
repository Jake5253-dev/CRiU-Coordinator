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
        
@app.command()
def printProcesses(returnData: bool = False):
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
        print(f"My process ID is {my_id}")
        if returnData:
            return python_process_list
        else:
            print(python_process_list)

@app.command()
def CRiU_Coordinator():
    print("Starting CRiU_Coordinator")
    process_list = printProcesses(returnData = True)
    print("Ending CRiU_Coordinator")


if __name__ == "__main__":
    app()
