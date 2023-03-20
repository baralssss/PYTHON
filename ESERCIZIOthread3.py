from threading import Thread
from time import sleep

class Task(Thread):
    def __init__(self, id, temp):
        Thread.__init__(self)
        self.id = id
        self.temp = temp
        
    def run(self):
        print(f'START THREAD {self.id}...')
        sleep(self.temp)
        print(f'FINISH THREAD {self.id}...')
        
        
class TaskCOUNT(Thread):
    def __init__(self, id, x):
        Thread.__init__(self)
        self.id = id
        self.x = x
        
    def run(self):
        for i in range(0, 20):
            self.x = self.x + 1
            sleep(1)
            print(f'THREAD {self.id} : {self.x}...')
        
def main():
    t1 = Task(1, 1)
    t1.start()
    
    t2 = TaskCOUNT(2, 0)
    t2.start()
    
    t1.join()
    t2.join()
    print("fine processo")
    
if __name__=="__main__":
    main()