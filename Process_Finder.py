import subprocess


class Process_Finder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        pass
    def get_process_list(self):
        pid_list = subprocess.run(["ps", "-lax", "grep", "main.py"], capture_output=True, text=True)
        print(pid_list)