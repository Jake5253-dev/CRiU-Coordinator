
import subprocess
import re
import os


class ProcessFinder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        
        self.__my_id = os.getpid()
        self.__list_of_processes: list[str] = self.__generate_process_list()

    def __generate_process_list(self):
        """ Generates a list of PIDs that are potential targets for stopping
        by CRIU CoOrdinator
        Invoked multiple times to regenerate list"""

        pid_list: subprocess.CompletedProcess = subprocess.run(["ps", "-lax"], capture_output=True, text=True)
        back_to_lines: list[str] = pid_list.stdout.splitlines()
        return self.__filter_process_list(back_to_lines)
        

    def __filter_process_list(self, unfiltered_list: list[str]) -> list:
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
        return_list: list[str] = []
        for line in string_list:
            self_pid = False
            split_list: list[str] = line.split()
            
            
            #This is the third item in the string, which is PID
            #Other columns may randomly be the same so we must target PID column only
            if split_list[2] == str(self.__my_id):
                self_pid= True

            if self_pid == False:
                return_list.append(line)
        return return_list

    def __header(self):
        return("List of Processes:\nF   UID     PID    PPID PRI  NI    VSZ   RSS WCHAN  STAT TTY        TIME COMMAND")

    def print_process_list(self):

        """Method prints the process list and what PID # is associated with CRIU CoOrdinator"""
        """ Prints directly to terminal"""
        print(self.__header())
        self.refresh_process_list()
        for process in self.__list_of_processes:
            print(process)
        print(f"my process id is {self.__my_id}")

    def get_process_list(self) -> list:
        self.refresh_process_list()
        return self.__list_of_processes

    def refresh_process_list(self):
        self.__list_of_processes = self.__generate_process_list()
