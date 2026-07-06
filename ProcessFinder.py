
import subprocess
import re
import os


class ProcessFinder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        #grabs the PID to allow elimination of itself from CRIU Dumping targets
        self.my_id = os.getpid()
        self.list_of_processes()

    def generate_process_list(self):
        """ Generates a list of PIDs that are potential targets for stopping
        by CRIU CoOrdinator"""

        pid_list: str = subprocess.run(["ps", "-lax"], capture_output=True, text=True)
        back_to_lines = pid_list.stdout.splitlines()
        self.list_of_processes = self.__filter_process_list(back_to_lines)
        

    def __filter_process_list(self, unfiltered_list: list) -> list:
        """Handles the filtering of the lists returned to get_process_list"""

        string_list: list = []

        #We are searching only for main.py strings as this is how we will run these processes
        process_identifier: str = "main.py"
        
        for line in unfiltered_list:
            if process_identifier in line:
                string_list.append(line)
        return self.__remove_self_pid(string_list)
        
    def __remove_self_pid(self, string_list: list) -> list:
        removed_self_pid_list = []
        for line in string_list:
            self_pid = False
            split_list = line.split()
            
            
            #This is the third item in the string, which is PID
            #Other columns may randomly be the same so we must target PID column only
            if split_list[2] == str(self.my_id):
                self_pid= True

            if self_pid == False:
                removed_self_pid_list.append(line)
        return removed_self_pid_list

    def __header(self):
        return("  F   UID     PID    PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND")

    def get_process_list(self):
        print(self.__header())
        print(self.generate_process_list)
        print(f"my process id is {self.my_id}")
