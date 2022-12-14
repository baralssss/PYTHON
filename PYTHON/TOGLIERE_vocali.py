vocali = ['a', 'e', 'i', 'o', 'u']

string = input("Inserisci una parola : ")

risp = True
lF = []
h = 0
list(string)

for i in range(0, len(string)):
    for j in range(0, len(vocali)):
        if string[i] == vocali[j]:
            risp = False
    if risp == True:
        lF[h].append(string[i])
        h = h+1

print(lF)