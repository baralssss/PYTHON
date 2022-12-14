#tuple = simili alle liste ma immutabili

punto = (1.5, 3.6) #si dichiara con le tonde (la lista si dichiara con le quadre)

print(f"La coordinata x del punto è : {punto[0]}") #si usa come lista con indicizzazione e slicing

triangolo = [(1.5, 3.6), (-1.0,0.0), (5.1,4.3)]
print(f"La coordinata y del secondo vertice è : {triangolo[1][1]}") #doppia indicizzazione = prima 1 per andare al secondo coordinate e poi 1 per la y

#Dizionari in python = contenitore più sofisticato (non valgono indicizzazione e slicing)

d = {1 : "Abello", 2 : "Armando"} #un'elemento si riconosce con la coppia chiave/valore

d2 = {"Abello" : [8, 9, 7, 10], "Armando" : [6, 8, 3, 9]} #dati molto strutturati --> i dati in rete viaggiano in strutture di dizionari annidati

#l'indicizzazione si fa mediante le chiavi --> indicizzazione sempre con le quadre
print(d[2])
print(d2["Abello"])