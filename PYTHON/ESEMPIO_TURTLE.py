import turtle

finestra = turtle.Screen() #creazione della finestra di disegno = per controllare la schermata
carlos = turtle.Turtle() #istanza turtle turtle

for i in range(0, 4):
    carlos.forward(100)
    carlos.right(90)
    carlos.forward(100)
    carlos.back(100)
    carlos.left(90)
    carlos.back(100)
    carlos.right(90)
    carlos.circle(100)
    carlos.circle(89)


turtle.done()