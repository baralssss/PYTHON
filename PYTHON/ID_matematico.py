matematici = {1 : "Gauss", 2 : "Eulero", 3 : "Euclide", 4 : "Pitagora", 5 : "Cartesio", 6 : "Archimede"}

ID = int(input("Inserisci l'id del matematico da cercare : "))

for i in range (1, 6):
    if ID == i:
        print(matematici[i])
    