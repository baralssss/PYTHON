def main():
    file = open("./matematici.csv")
    righe = file.readlines()
    file.close()
    diz = {"id" : [], "nome" : []}
    
    for riga in righe[1:]:
        campi_riga = riga[:-1].split(",")
        diz["id"].append(int(campi_riga[0]))
        diz["nome"].append(campi_riga[1][1:])
    print(diz)
        

if __name__=="__main__":
    main()