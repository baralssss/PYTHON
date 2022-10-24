lista = [100, 34, 76, 89]

#modo preferito (pythonico)
#in python l'indentazione è sintattica = da un significato = le graffe del C sono l'indentazione del python
for elemento in lista:
    print(elemento)
    
#modo C style

for i in range(0, len(lista)):
    print(lista[i], end = "-") #end per non fare andare = cambio carattere di fine print (di default è \n)
    
#calcolo max e min + stampa
minimo = lista[0]
massimo = lista[0]
for elemento in lista[1:]:
    if minimo > elemento:
        minimo = elemento
    else:
        pass
    if massimo < elemento:
        massimo = elemento
print("\n")       
print(minimo)
print(massimo)

#for con enumerate

for i, e in enumerate(lista):
    print(i, e)
    
#while -->

while condizione:
    codice
    
#pass = non fa nulla = per riempire codice
#break = interrompe il primo ciclo rispetto alla sua chiamata
#continue = fa saltare un giro al ciclo
#tutte le funzioni di un robot sono racchiuse in un while true: --> ripete all'infinito il funzionamento del robot --> break per fermare l'azione del robot in situazione di pericolo

#definizione funzione --> nome(parametro, parametro):
                                   #codice indentato
                                   #return tutte le variabili che voglio (non più solo una come in c)
                                   
#Nel main -->
#x, y = nome(parametro, parametro)
