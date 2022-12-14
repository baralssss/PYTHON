def leggi_file(nome_fp):
    file = open(nome_fp,"r")
    lista_righe=file.readlines()
    file.close()

    diz_nomi={}

    for riga in lista_righe[1:]:
        lista_campi = riga[:-1].split(",")

        diz_nomi[int(lista_campi[0])]=lista_campi[1]

    return diz_nomi

def nomeID(id,diz):
    
    for k,v in diz.items():
        #print(k)
        if(k==id):
            return(v)

def main():
    diz_nomi = leggi_file("file.csv")
    print (diz_nomi)

    id = 4

    print(nomeID(id,diz_nomi))

if _name=="main":#nella variabile __name_ si salva il nome del programma chiamante
    main()              #se il nome è uguale esegue