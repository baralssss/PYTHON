n = int(input("Inserisci un numero : "))
l = []

for i in range(1, n+1):
    l.append(i)
    
print(l)

#modo veloce = list comprehension = costruisce una lista al volo

l1 = [j for j in range(1, n+1)]
print(l1)

