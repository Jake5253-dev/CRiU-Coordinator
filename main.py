import typer
import os
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
def printDirectory():
    name = os.listdir()
    print("Here is a list of all files")
    for file in name:
        print(str(file)+ "\n")
        
@app.command()
def printProcesses():
    pid_list = os.listdir('/proc')
    print(pid_list)


if __name__ == "__main__":
    app()
