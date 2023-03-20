from threading import Thread
from time import sleep
import random

class Task(Thread):
    def __init__(self, id):
        Thread._init_(self)
        self.id = id
    
    def run(self):
        print(f"START thread id = {self.id}")
        if self.id == 0:
            for n in range(0, 21, 2):
                print(f"numero pari {n}")
                sleep(0.00001)
        elif self.id == 1:
            for n in range(1, 20, 2):
                print(f"numero dispari {n}")
                sleep(0.00001)
        sleep(0.0001)
        print(f"FINISH thread id = {self.id}")

l = [Task(id) for id in range(10)]

for t in l:
    t.start()
for t in l:
    t.join()