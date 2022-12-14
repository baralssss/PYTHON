def leggiFile(nome_file):
    file=open(nome_file, "r")
    lista_righe= file.readlines()
    print(lista_righe)
    file.close()
    
    diz_mat={"data":[], "cognome":[], "quota":[]} #id sono numeri, nomi sono stringhe 
    #print(diz_mat)
    #exit()
    sommaTot=2200 #preferibile scrivere le costanti come variabili con nome tutto maiuscolo
    sommaPTot=100
    sommaP=0
    somma=0
    for riga in lista_righe[:]:
        if(riga[-1]=="\n"):
            riga_senza_linefeed=riga[:-1] #senza \n
        else: riga_senza_linefeed=riga
        #print(riga_senza_linefeed)
        lista_campi=riga_senza_linefeed.split(";")
        #print(lista_campi)
        data=lista_campi[0]
        cognome=lista_campi[1]
        quota=lista_campi[2]
        #print(id, nome)
        diz_mat["data"].append(data)
        diz_mat["cognome"].append(cognome)
        diz_mat["quota"].append(int(quota))
        somma+=int(quota)
        if(cognome=="Abello"):
            sommaP+=int(quota)

    #print(somma)
    if somma==sommaTot:
        print(f"Totale corretto")
    else:
        if somma>sommaTot: 
            print(f"Sono presenti {somma-sommaTot} euro in più")   
        else: print(f"sono presenti {sommaTot-somma} euro in meno")
    print()
    if(sommaP==sommaPTot): print(f"Pagato tutta la quota")
    else: print(f"Controllare la quota versata") 
    print()  


    return diz_mat
def trovaIndice(lista_cognome1, k):
    for count, c in enumerate(lista_cognome1):
        if c==k: return count
 


def pagamento(diz):
    lista_cognome=diz["cognome"]
    lista_quota=diz["quota"]
    lista_cognome1=[]
    lista_quota1=[]
    
    c=0
    for k, v in zip(lista_cognome, lista_quota):
        if not k in lista_cognome1: #espressione booleana = true se è dentro la lista, altrimenti for --> con il not davanti controllo che il cognome non sia in lista cognomi
            lista_cognome1.append(k)
            lista_quota1.append(v)
        else:
            i=trovaIndice(lista_cognome1, k)
            lista_quota1[i]+=v
    for cogn, qu in zip(lista_cognome1, lista_quota1):
        print(cogn, qu)
        if qu!=100: print(f"--> da controllare")

def main():
    diz=leggiFile("4AROB_GITA.csv")
    #print(diz)
    pagamento(diz)

if __name__ =="__main__": #__dunder
    main()