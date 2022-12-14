def isPRIMO(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    else:
        return True

j = 0
lista = []

for a in range(0, 100):
    if isPRIMO(a) == True:
        lista.append(a)

print(lista)

#con list compr
n = 100
l = [i for i in range(2, n) if isPRIMO(i)]
print(l)
