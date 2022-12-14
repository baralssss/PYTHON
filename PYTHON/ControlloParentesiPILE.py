#s = input("inserisci la stringa da analizzare :")
with open('codice.txt', 'r') as file:
    s = file.read().replace('\n', '')

pila = []

print(s)
for i in s:
    if i == "(":
        pila.append(i)
    elif i == "[":
        pila.append(i)
    elif i == "{":
        pila.append(i)
    elif i == ")":
        a = pila.pop()
    elif i == "]":
        b = pila.pop()
    elif i == "}":
        c = pila.pop()
print(pila)
if(len(pila) > 0):
    print(f"errore nella chiusura delle parentesi, aperta : {pila} e non chiusa")
print(s)
