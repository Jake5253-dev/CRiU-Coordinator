class CriuRunner:

    """Performs the loop to run the Criu CoOrdinator"""

    def __init__(self):
        self.active_daemon_PID: list
        self.dumps: list
        running: bool



    def command_loop(self):
        running = True
        while running:
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
                    continue
                case _:
                    print("Please select an avaliable option")
                    continue

    def dump_process(self):
        print("activated dumping processes")

    def restore_process(self):
        print("activated restoring a process")

    


        
