from threading import Thread
from time import sleep

#posso lavorare con più classi thread contemporaneamente
class Task(Thread):
    def __init__(self, id, temp):
        Thread.__init__(self)
        self.id = id
        self.temp = temp #tempo attesa per la sleep
        
    def run(self):
        print(f'START THREAD {self.id}...')
        sleep(self.temp)
        print(f'FINISH THREAD {self.id}...')
        
        
class Task2(Thread):
    def __init__(self, id, temp):
        Thread.__init__(self)
        self.id = id
        self.temp = temp #tempo attesa per la sleep
        
    def run(self):
        print(f'START THREAD {self.id}...')
        sleep(self.temp)
        print(f'FINISH THREAD {self.id}...')
        

def main():
    t1 = Task(1, 3)
    t1.start() #parte il metodo run()
    
    t2 = Task(2, 3)
    t2.start()
    
    t3 = Task(3, 3)
    t3.start()
    
    t1.join()#attnede la fine del thread
    t2.join()
    t3.join()
    
    print('FINITA ESECUZIONE')
    
if __name__=="__main__":
    main()