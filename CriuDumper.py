import os
import subprocess
from datetime import datetime


class CriuDumper:
    """ Criu Dumping class, takes in a PID and moves the dumped PID contents to a folder"""

    def __init__(self):

        self.__dump_folder_path_string: str = os.getcwd()+ "/CriuDumps"
        if not  os.path.exists(self.__dump_folder_path_string):
            os.mkdir(self.__dump_folder_path_string)


    def dump_daemon_process(self, PID_num: str):

        """ dumps a running Daemon process, meaning that the standard input, output and error are not collected anywhere
        and process is started as a new session, not connected to a terminal
        Moves the dump into a local sub folder called CriuDumps, and generates a folder to store the contents of the dump """

        folder_name: str = self.__create_folder_for_PID(PID_num)
        #TODO: remove dump log generation and associated methods
        self.__dump_logging_new_entry()
        result: subprocess.CompletedProcess = subprocess.run(["sudo", "criu", "dump", "-t", str(PID_num)
        ,"-D", str(folder_name), "-vvv", "--log-file", "dump_details.txt"])
        if result.returncode == 0:
            print("OK")
        else:
            print("Dumping Failed")
    
    def __return_criu_dump_folder(self) -> str:
        return self.__dump_folder_path_string

    def __dump_logging_new_entry(self):
        with open("dump_log.txt","a") as f:
            f.write(self.__new_dump_log_paragraph())

    def __new_dump_log_paragraph(self) -> str:
        formatting_string = "-------------------\n New Entry\n -------------------\n"
        return formatting_string

    def __create_folder_for_PID(self, PID_num: str) -> str:
        """Creates a unique folder for the PID dump, based on PID ID and datetime.now details.
        Returns the directory path of newly created folder"""

        now = datetime.now()
        # format day, three letter month, year, hrs, mins, secs, milisecs
        new_folder_string: str = "PID_" + PID_num + "__" + now.strftime("%d-%b-%Y__%Hhrs-%Mmin-%Ssec-%fms")
        return_string: str = self.__dump_folder_path_string + "/" + new_folder_string
        os.mkdir(return_string)
        return return_string
