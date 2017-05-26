import threading
import time

class TimerClass(threading.Thread):
    """Class to excecute a function at
    different time with config

    Ex: my_function = main_excecution
    config = openface_config.yml (config file)

    """
    def __init__(self, step, my_function, config):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.count = 10
        self.step = step
        self.my_function = my_function
        self.config = config

    def run(self):
        while self.count > 0 and not self.event.is_set():
            #print(self.count)
            self.my_function(self.config)
            #self.count -= 1
            self.event.wait(self.step)

    def stop(self):
        self.event.set()

if __name__ == '__main__':

    coco = print

    tmr = TimerClass(1, coco, "lol")

    tmr.start()

    #time.sleep(10)

    tmr.stop()
