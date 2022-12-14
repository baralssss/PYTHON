class Robot():
    def __init__(self, massa, nome, umanTF):
        self.massa = massa #stringa
        self.nome = nome #nome
        self.umanTF = umanTF #bool
        
    def printNome(self):
        print(self.nome)
        
    def iSpericoloso(self):
        if self.umanTF == True and self.massa >= 100: #se un metodo calcola qualcosa restituisce il risultato del calcolo
            return True
        else:
            return False

def main():
    massa = int(input("Inserisci la massa del robot : "))
    nome = input("Inserisci il nome del robot : ")
    umanTF = False
    robot = Robot(massa, nome, umanTF)
    robot.printNome()
    if robot.iSpericoloso():
        print("Il robot è pericoloso")
    else:
        print("Il robot non è pericoloso")
        
        pr
    
if __name__ == '__main__':
    main()