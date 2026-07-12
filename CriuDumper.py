import os


class CriuDumper:
    """ Criu Dumping class, takes in a PID and moves the dumped PID contents to a folder"""

    def __init__(self):
        pass


    def dump_daemon_process(PID_num: String):

        """ stops a running Daemon process, meaning that the standard input, output and error are not collected anywhere
        and process is started as a new session, not connected to a terminal"""

        #Stores the dump in a sub folder called criu_holding
        #TODO create a more sophisticated dump file storage system

        PID = PID_num 
        result = subprocess.run(["sudo", "criu", "dump", "-t", str(PID), "-D", "criu_holding", "-vvv"])
        if result.returncode == 0:
            print("OK")
        else:
            print("Dumping Failed")
    def select_criu_dump_folder(self):
        
        path_string = os.getcwd()+ "/CriuDumps"

       if not  os.path.exists(path_string):
            os.mkdir(path_string)
        
        print("Entered select_criu_dump_foler")
        print(os.getcwd())
        print(os.getcwd() + "CriuDumps")

    def dump_logging(Criu_dump_log: String):
        with open("dump_log.txt") as f:
            f.write(new_dump_log_paragraph())
            f.write(Criu_dump_log)

    def new_dump_log_paragraph():
        
        formatting_string = "-------------------\n New Entry\n -------------------\n"

        return formatting_string
