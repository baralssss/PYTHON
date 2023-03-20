DIM = 8
LARG = 4
SPAZ = 2
LUNG = 100
NBAR = 64

class Barcode():
    def __init__(self, string):
        self.string = string
        self.ascii = None
        self.bin = None
    
    def string2ascii(self): #classe per la creazione di stringa ascii = ogni valore ascii di ogni carattere è separato da punto
        ascii1 = ""
        for car in self.string:
            if ord(car) < 255:
                ascii1 = ascii1 + str(ord(car)) + "." #funzione ord che nel ciclo for prende come parametro i caratteri della stringa
        self.ascii = ascii1[:-1] #considero tutta la stringa escludendo il punto finale tramire lo slicing
        return self.ascii
    
    def ascii2bin(self):
        bin1 = self.ascii.split(".")  #splitto gli interi della conversione ascii separati dai punti
        lista_grupp = [int(Bin)for Bin in bin1] #con una list comp creo una lista dei valori da scorrere con un for
        s = ""
        self.bin = ""
        for gruppo in lista_grupp:
            temp= bin(gruppo)[2:]
            temp = "0"*(8-len(temp))+temp #ad ogni conversione aggiungo quanti "0" mancano per arrivare a 8 bit
            self.bin = self.bin + temp #salvo la stringa
            s = s + temp
        return s[:-1]
    
    def drawBarCode(self):
        import turtle  #chiamata in utilizzo della libreria turtle
        finestra = turtle.Screen()
        carlos = turtle.Turtle()
        carlos.pensize(LARG)
        carlos.speed(0)
        carlos.pendown()
        #print(self.bin)
        for n in self.bin: #scorro la stringa in codifica binaria e a seconda del carattere creo barre o nere o bianche utilizzando le funzioni della turtle
            if n == "0":
                carlos.pencolor("white")
                carlos.right(90)
                carlos.forward(LUNG)
                carlos.penup()
                carlos.back(LUNG)
                carlos.left(90)
                carlos.forward(SPAZ)
                carlos.pendown()
            elif n == "1":
                carlos.pencolor("black")
                carlos.right(90)
                carlos.forward(LUNG)
                carlos.penup()
                carlos.back(LUNG)
                carlos.left(90)
                carlos.forward(SPAZ)
                carlos.pendown()
                
        turtle.done()
        
    
def main():
    string = input("Inserisci la stringa alfanumerica di 8 caratteri :")
    if(len(string) > 8):
        print("Stringa non accettata")
    else:
        barcode = Barcode(string)
        print(f"Conversione ascii: {barcode.string2ascii()}\n") #stampo i vari dati di conversione
        print(f"Conversione binaria: {barcode.ascii2bin()}\n")
        barcode.drawBarCode() #chiamo la funzione per disegnare il barcode
        

if __name__ == '__main__':
    main() 