import subprocess
import re


class Process_Finder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        pass
    def get_process_list(self):
        pid_list: str = subprocess.run(["ps", "-lax", "|", "grep", "main.py"], capture_output=True, text=True)
        filtered_pid_list = filter_process_list(pid_list)

        print(filtered_pid_list)
    def filter_process_list(self, unfiltered_list: str) -> str:
        string_list: list
        process_identifier: str = "main.py"
        for line in unfiltered_list:
            if process_identifier in line:
                string_list.append(line)
        
        return string_list

