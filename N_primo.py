n = int(input("Inserici un numero : "))

if n <= 1:
    print("Il numero deve essere maggiore di 1.")

else:    
    div,cont = 2, 0

    while div <= n/2 and cont == 0:
        if n % div == 0:
            cont = cont + 1
    
    div = div + 1
     

        
    if cont == 0:
        print("Il numero e' primo")
    else:
        print("Il numero non e' primo")
    