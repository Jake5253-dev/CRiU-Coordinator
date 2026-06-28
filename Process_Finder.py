import subprocess
import re


class Process_Finder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        pass
    def get_process_list(self):
        pid_list: str = subprocess.run(["ps", "-lax"], capture_output=True, text=True)
        back_to_lines = pid_list.stdout.splitlines()
        #for line in back_to_lines:
        #    print(line)

        filtered_pid_list = self.filter_process_list(back_to_lines)

        print(filtered_pid_list)
    def filter_process_list(self, unfiltered_list: list) -> list:
        string_list: list = []
        process_identifier: str = "main.py"
        for line in unfiltered_list:
            if process_identifier in line:
                string_list.append(line)
        
        return string_list

