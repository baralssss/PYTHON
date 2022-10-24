#nel messaggio ogni lettera è sostituita con la lettera successiva dell'alfabeto, lo spazio resta spazio

parola = input("Inserisci il messagio da codificare : ")
alfabeto = {" " : " ", "a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "g", "g" : "h", "h" : "i", "i" : "j", "j" : "k", "k" : "l", "l" : "m", "m" : "n", "n" : "o", "o" : "p", "p" : "q", "q" : "r", "r" : "s", "s" : "t", "t" : "u", "u" : "v", "v" : "w", "w" : "x", "x" : "y", "y" : "z", "z" : "a"}
alfabeto1 = {" " : " ", "b" : "a", "c" : "b", "d" : "c", "e" : "d", "f" : "e", "g" : "f", "h" : "g", "i" : "h", "j" : "i", "k" : "j", "l" : "k", "m" : "l", "n" : "m", "o" : "n", "p" : "o", "q" : "p", "r" : "q", "s" : "r", "t" : "s", "u" : "t", "v" : "u", "w" : "v", "x" : "w", "y" : "x", "z" : "y", "a" : "z"}
codifica = ""
decodifica = ""

for lettera in parola:
    codifica = codifica + alfabeto[lettera]

print(codifica)

for lettera in codifica:
    decodifica = decodifica + alfabeto1[lettera]
    
print(decodifica)

#cicli for anche su più variabili simultaneamente
decodificatore = {} #dizionario vuoto

for k,v in alfabeto.items(): #k = chiave v = valore
    decodificatore[v] = k
 
decodifica1 = ""
   
for lettera in codifica:
    decodifica1 = decodifica1 + decodificatore[lettera]
    
print(decodifica1)
