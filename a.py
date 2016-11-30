import subprocess, threading
import random
import os


#to execute the run_command in solver
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return [item.strip() for item in iter(p.stdout.readline, b'')]










#to be used for solver where a command needs to be executed
class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
        self.process_lock = threading.Lock()
        self.output = ""

    def run(self):
        
        def target():
            self.process_lock.acquire()
            if self.process is None:
                self.process = subprocess.Popen(self.cmd,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.STDOUT)
                self.process_lock.release()
                self.output, err = self.process.communicate()
            else:
                self.process_lock.release()

        thread = threading.Thread(target=target)
        thread.start()
        
        if thread.is_alive():
            self.process_lock.acquire()
            if self.process is not None:
                try:
                    self.process.kill()
                except:
                    pass
            self.process = False
            self.process_lock.release()
            thread.join()
            return None
        return self.output



filename = "tmp/SAT_test.cnf"
solver = Command(['./cryptominisat5', ' --verb=0 ', filename])
result = solver.run()

#result = result.split()
print("Result = "+str(result))
#outcome = result[1]
#print("Result = "+str(outcome))


