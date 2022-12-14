a = [1, 2, 3, 4, 5, 6]
b = a #sono due puntatori --> se modifichiamo b si modifica anche a e viceversa
b[0] = 999
c = a.copy() #crea lista indipendente = copia di a

c[0] = 1111

print(a)
print(c)

print(a.pop(2))