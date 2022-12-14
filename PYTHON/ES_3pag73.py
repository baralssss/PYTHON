import random

def eseguioperazione(noperazione, n1, n2):
    if(noperazione == 0):
        return n1 + n2
    elif(noperazione == 1):
        return n1 - n2
    elif (noperazione == 2):
        return n1 * n2
    elif (noperazione == 3):
        return n1 / n2

noperazione = random.randint(0,3)
n1 = int(input("inserisci il primo numero: "))
n2 = int(input("inserisci il secondo numero: "))

print("il valore dell'operazione scelta e': ")
print(eseguioperazione(noperazione, n1, n2))