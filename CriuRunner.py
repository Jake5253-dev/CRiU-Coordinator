from CriuDumper import CriuDumper
from CriuRestorer import CriuRestorer
from ProcessFinder import ProcessFinder

class CriuRunner:

    """Performs the loop to run the Criu CoOrdinator"""

    def __init__(self):
        self.cd = CriuDumper()
        self.pf = ProcessFinder()
        self.cr = CriuRestorer()
        
        self.active_daemon_PID = self.pf.get_process_list()
        self.dumps: list
        
        



    def command_loop(self):
        running = True
        while running:
            print("")
            self.pf.print_process_list()
            print("Please choose an option from the following list:")
            print("1: dump a process")
            print("2: restore a process")
            print("3: exit")
            response = input()
            
            match response:
                case "1":
                    self.dump_process()
                case "2":
                    self.restore_process()
                case "3":
                    running = False
                    print("Shutting down CRiU CoOridnator")
                    continue
                case _:
                    print("Please select an avaliable option")
                    continue

    def dump_process(self):
        print("")
        print("Please select a process to stop:")
        if not self.active_daemon_PID:
            print("There are no processes to stop")
        else:
            process_dict = {}
            count = 0
            for process in self.active_daemon_PID:
                count = count + 1
                process_string_list = process.split()
                process_dict[count] = process_string_list[2]
            for key, value in process_dict.items():
                print(f"{key}: {value}")
            PID_to_stop = input("Which process would you like to stop?")
            PID_int = int(PID_to_stop)
            self.cd.dump_daemon_process(process_dict.get(PID_int))
            self.active_daemon_PID = self.pf.get_process_list()

        # self.cd.dump_daemon_process()
        
    def restore_process(self):
        cr.__get_list_of_dump_files()

    def PID_validation(self):
        pass
        #TODO create a validator of inputs

