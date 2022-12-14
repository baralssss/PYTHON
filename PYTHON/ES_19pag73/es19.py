import random

def scriviFile(name_file, Juan, Carlos):
    f = open(name_file, "w")
    

    for i, j in zip(Juan, Carlos):
        f.write(f"{Juan[i]}, {Carlos[j]}\n")

    f.close()

def main():
    Juan = [random.randint(1, 6) for i in range(10)]
    Carlos = [random.randint(1, 6) for i in range(10)]
    name_file = "file.txt"
    
    scriviFile(name_file, Juan, Carlos)

if __name__ == "__main__":
    main()