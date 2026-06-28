import subprocess
import re
import os


class ProcessFinder:
    """Class that finds all current processes within the
    VM enviroment it finds itself in"""

    def __init__(self):
        #grabs the PID to allow elimination of itself from CRIU Dumping targets
        self.my_id = self._set_my_id()

    def get_process_list(self):
        """ Generates a list of PIDs that are potential targets for stopping
        by CRIU CoOrdinator"""

        pid_list: str = subprocess.run(["ps", "-lax"], capture_output=True, text=True)
        back_to_lines = pid_list.stdout.splitlines()
        filtered_pid_list = self.filter_process_list(back_to_lines)
        print(_filtered_pid_list)
    def _filter_process_list(self, unfiltered_list: list) -> list:
        """Handles the filtering of the lists returned to get_process_list"""

        string_list: list = []

        #We are searching only for main.py strings as this is how we will run these processes
        process_identifier: str = "main.py"
        
        for line in unfiltered_list:
            if process_identifier in line:
                string_list.append(line)
        
        

        return _remove_self_pid(string_list)
        
    def _remove_self_pid(self, string_list: list) -> list:
        removed_self_pid_list = []
        for line in string_list:
            self_pid = False
            split_list = line.split()
            
            for line in split_list:
                if line == str(self.my_id):
                    self_pid = True
                    break
            

            if self_pid == False:
                removed_self_pid_list.append(line)
                
        return removed_self_pid_list


    def _set_my_id(self):
        self.my_id = os.getpid()



