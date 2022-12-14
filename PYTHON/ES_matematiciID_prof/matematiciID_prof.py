def leggiFILE():
    file = open("./matematici.csv")
    righe = file.readlines()
    file.close()
    diz = {"id" : [], "nome" : []}
    
    for riga in righe[1:]:
        campi_riga = riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1][1:])
    return diz
  
def nomeID(id, diz):
    listaID = diz["id"]
    listaNOMI = diz["nome"]
    for i, n in zip(listaID, listaNOMI): #a zip passo 2 liste da scorrere (2 contatoti) e zip scorre parallelamente le liste
        if i == id:
            return n

def main():
    diz = leggiFILE()
    id = 2
    nome = nomeID(id, diz)
    print(nome)      

if __name__=="__main__":
    main()