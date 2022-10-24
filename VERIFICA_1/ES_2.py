n = int(input("Inserisci un numero : "))

lista = [1]*n

lista[0], lista[-1] = 0, 0

print(lista)