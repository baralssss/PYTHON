import turtle
from random import seed
from random import randint

SPEED = 10000
MS = 3600000
MOV = 5

finestra = turtle.Screen()
pablo = turtle.Turtle()

def main():
    finestra.screensize(1000, 1000, "black")
    seed(1) #generazione di numeri è sempre la stessa
    pablo.color("yellow")
    pablo.speed(SPEED)
    for i in range(0, MS):
        n = randint(0, 4)
        angolo = 90*n
        pablo.right(angolo)
        pablo.forward(MOV)
        
    turtle.done()
       
if __name__=="__main__":
    main()