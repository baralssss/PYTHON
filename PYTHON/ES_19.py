#chiedo due numeri = dizionari con 2 elementi uno media aritmetice e secondo media geometrica

n1 = int(input("Inserisci il primo numero : "))
n2 = int(input("Inserisci il secondo numero : "))

medie = {"Media Arit" : (n1 + n2)/2, "Media Geom" : (n1 * n2)**0.5}

print(medie)