def scriviFile(nome_file):
    f = open(nome_file, "w")
    for i in range(1, 11):
        for j in range(1, 11):
            f.write(f"\t{i * j} ")
        f.write("\n")
    f.close()

def main():
    tavola_pitagorica = []
    scriviFile("file.txt")
if __name__ == "__main__":
    main()