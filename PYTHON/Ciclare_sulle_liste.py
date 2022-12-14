lista1 = ["a", "b", "c", "d"]
lista2 = [1,2,3,4]

#for su lista1 C-style
print("Su lista1 C-style")
for i in range(0, len(lista1)):
    print(lista1[i])

#for su lista1 Python-style
print("Su lista1 Python-style")
for elemento in lista1:
    print(elemento)
    
#for su lista1 con enumerate = cicla sia su indice che su elemento
print("Su lista1 con enumerate")
for i, elemento in enumerate(lista1):
    print(elemento)
#for su lista1 e lista2 Python-style (zip) = al posto di i e n posso usare una tupla elemento --> elemento = (i, n)
print("Su lista1 e lista2 con zip")
for i, n in zip(lista1, lista2):
    print(i, n)
#for su lista1 e lista2 C-style (range..)
print("Su lista1 e lista2 C-style")
for i in range(0, len(lista1)):
    print(lista1[i], lista2[i])

diz = {1 : "billone", 2 : "uaglione"}

#for su diz con items()
print("Su diz con items()")
for chiave, valore in diz.items():
    print(chiave, valore)

#for su diz senza items()
print("Su diz senza items con stampa chiave")
for chiave in diz:
    print(chiave)

print("Su diz senza items con stampa elemento")
for chiave in diz:
    print(diz[chiave])
    