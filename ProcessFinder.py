
import subprocess
import re
import os


class ProcessFinder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        
        self.my_id = os.getpid()
        self.list_of_processes = self.__generate_process_list()

    def __generate_process_list(self):
        """ Generates a list of PIDs that are potential targets for stopping
        by CRIU CoOrdinator"""

        pid_list: str = subprocess.run(["ps", "-lax"], capture_output=True, text=True)
        back_to_lines = pid_list.stdout.splitlines()
        return self.__filter_process_list(back_to_lines)
        

    def __filter_process_list(self, unfiltered_list: list) -> list:
        """Handles the filtering of the lists returned to __generate_process_list"""

        string_list: list = []

        #We are searching only for main.py strings as this is how we will run these processes
        process_identifier: str = "main.py"
        
        for line in unfiltered_list:
            if process_identifier in line:
                string_list.append(line)
        return self.__remove_self_pid(string_list)
        
    def __remove_self_pid(self, string_list: list) -> list:

        """ Removes the Processes's own PID as we don't want this to be dumped""" 
        return_list = []
        for line in string_list:
            self_pid = False
            split_list = line.split()
            
            
            #This is the third item in the string, which is PID
            #Other columns may randomly be the same so we must target PID column only
            if split_list[2] == str(self.my_id):
                self_pid= True

            if self_pid == False:
                return_list.append(line)
        return return_list

    def __header(self):
        return("F   UID     PID    PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND")

    def get_process_list(self):

        """Method prints the process list and what PID # is associated with CRIU CoOrdinator"""
        print(self.__header())
        for process in self.list_of_processes:
            print(process)
        print(f"my process id is {self.my_id}")
