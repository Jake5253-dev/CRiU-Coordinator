import os
import subprocess
from datetime import date


class CriuDumper:
    """ Criu Dumping class, takes in a PID and moves the dumped PID contents to a folder"""

    def __init__(self):

        self.dump_folder_path_string= os.getcwd()+ "/CriuDumps"
        if not  os.path.exists(self.dump_folder_path_string):
            os.mkdir(self.dump_folder_path_string)


    def dump_daemon_process(self, PID_num: str):

        """ stops a running Daemon process, meaning that the standard input, output and error are not collected anywhere
        and process is started as a new session, not connected to a terminal"""

        #Stores the dump in a sub folder called criu_holding
        #TODO create a more sophisticated dump file storage system
        folder_name = __create_folder_for_PID(PID_num)
        result = subprocess.run(["sudo", "criu", "dump", "-t", str(PID_num)
        ,"-D", str(folder_name), "-vvv"])
        if result.returncode == 0:
            print("OK")
        else:
            print("Dumping Failed")
    
    def __return_criu_dump_folder(self):
        return self.dump_folder_path_string

    def __dump_logging(self, Criu_dump_log: String):
        with open("dump_log.txt") as f:
            f.write(__new_dump_log_paragraph())
            f.write(Criu_dump_log)

    def __new_dump_log_paragraph(self):
        formatting_string = "-------------------\n New Entry\n -------------------\n"
        return formatting_string

    def __create_folder_for_PID(self, PID_num: str) -> str:

        now = datetime.now()
        # SHould be day, 3 letter month, year, hour minute second then ms then miliseconds 
        new_folder_string = "PID " + PID_num + " " + now.strftime("%d-%b-%Y %H-%M-%S ms %f")
        return_string = self.dump_folder_path_string + "/" + new_folder_string
        os.mkdir(return_string)
        return return_string
