def ricercaSEQ(s):
    verifica = "ATGTTTGTTTTT" #stringa da cercare, pensavo di splittare s in blocchi da 12 bit e verificare blocco per blocco con un for
    for n in s.split():
        pass
    

def main():
    with open('covid-19_gen1.txt', 'r') as file: #funzione per lettura file comprendente apertura e chiusura
        s = file.read().replace('\n', ' ') #sostituzione degli \n per unificare il file in una stringa
    cA = 0
    cC = 0
    cG = 0
    cT = 0
    for car in s:  #scorro la stringa intera e verifico l'uguaglianza con i caratteri per aumentare dei contatori
        if car == "A":
            cA+=1
        elif car == "C": 
            cC+=1
        elif car == "G":
            cG+=1
        elif car == "T":
            cT+=1
    print(f"Numero A : {cA}, Numero C : {cC}, Numero G : {cG} e Numero T : {cT}") #stampo i contatori contenenti le occorrenze
    ricercaSEQ(s)
    

if __name__ == '__main__':
    main()