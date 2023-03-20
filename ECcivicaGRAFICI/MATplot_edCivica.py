import matplotlib.pyplot as plt
import csv

mesi_n = []
Giornigiacca = []
Temperature = []
GiorniScuola = []
GiorniVG = []
data_file = open('barale.csv')
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)
for row in data_reader:
     mesi_n.append(int(row[1]))
     Giornigiacca.append(float(row[2]))
     Temperature.append(float(row[3]))
     GiorniScuola.append(float(row[4]))
     GiorniVG.append(float(row[5]))
     
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
fig.suptitle('RICERCA DATI 1')

ax1.plot(mesi_n, Temperature, 'o-g')
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperature')

ax2.plot(mesi_n, Giornigiacca, 'o-r')
ax2.set_xlabel('Mese')
ax2.set_ylabel('Giorni giacca')

ax3.plot(mesi_n, GiorniScuola, 'o-r')
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni scuola')

ax4.plot(mesi_n, GiorniVG, 'o-r')
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni videogame')

plt.show()