import turtle
from random import seed
from random import randint
#disegnare 9 figure geometriche a partire dal triangolo e aumentando di un lato man mano

finestra = turtle.Screen() #creazione della finestra di disegno = per controllare la schermata
carlos = turtle.Turtle() #istanza turtle turtle

def poligono(gradi, lati):
    carlos.pensize(4)
    g = gradi / lati
    l = 50 - 15
    for k in range(0, lati):
        carlos.forward(l)
        carlos.right(g)

def main():
    finestra.screensize(1000, 1000, "black")
    seed(1)
    gradi = 360
    lati = 3
    for i in range(0,9):
        x1 = randint(-250, 250)
        y2 = randint(-250, 250)
        carlos.speed(500)
        carlos.color("pink")
        carlos.fillcolor("yellow")
        carlos.begin_fill()
        poligono(gradi, lati)
        carlos.penup()
        carlos.goto(x1, y2)
        carlos.pendown()
        lati+=1
        carlos.end_fill()
    turtle.done()
       
if __name__=="__main__":
    main()