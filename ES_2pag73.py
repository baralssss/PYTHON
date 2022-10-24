while True:
    x = int(input("Inserisci il numero da verificare : "))
    
    if x % 2 == 0:
        print("Il numero è divisibile per 2.")
    elif x % 3 == 0:
        print("Il numero è divisibile per 3.")
    elif x % 5 == 0:
        print("Il numero è divisibile per 5.")
    else:
        print("Il numero non è divisibile per nessuno dei numeri.")