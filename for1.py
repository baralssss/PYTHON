dizionario = {"w" : "avanti", "a" : "sinistra", "s" : "indietro", "j" : "avanti", "d" : "destra", "g" : "avanti", "z" : "avanti"}

for chiave in dizionario: #cicla solo per la chiave --> per chiave e valore = .items() --> per scorrere solo dati = dizionario[chiave]
    print(chiave)
    
#avendo solo elemento non posso risalire alla chiave

comando = "avanti"
lista = []

for chiave in dizionario:
    if dizionario[chiave] == comando:
        lista.append(chiave) #append = aggiunge un'elemento
        
print(lista)
    