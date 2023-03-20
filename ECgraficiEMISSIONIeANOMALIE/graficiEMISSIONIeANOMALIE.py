import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Temperature_Anomaly.csv')#uso la libreria pandas per leggere e gestire il csv per colonne
Year = df.Year
Value = df.Value 

df1 = pd.read_csv('CO2_emissions.csv')
Year1 = df1.Year
Total = df1.Total
GasFuel = df1.GasFuel
LiquidFuel = df1.LiquidFuel
SolidFuel = df1.SolidFuel
Cement = df1.Cement
GasFlaring = df1.GasFlaring
PerCapita = df1.PerCapita
     
fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8, 1)
fig.suptitle('ANOMALIE DELLA TEMPERATURA dal 1880 e EMISSIONI CO2')

ax1.plot(Year, Value, 'o-y') #plot per anomalie della temperatura
ax1.set_xlabel('Anni')
ax1.set_ylabel('Variazione')

ax2.plot(Year1, Total, 'o-r') #plot per valore emissioni totali
ax2.set_xlabel('Anni')
ax2.set_ylabel('Emissioni')

ax3.plot(Year1, GasFuel, 'o-r') #plot combustibili gassosi
ax3.set_xlabel('Anni')
ax3.set_ylabel('Gas')

ax4.plot(Year1, LiquidFuel, 'o-r') #plot per combustibili liquidi
ax4.set_xlabel('Anni')
ax4.set_ylabel('Liquid')

ax5.plot(Year1, SolidFuel, 'o-r') #plot per combustibili solidi
ax5.set_xlabel('Anni')
ax5.set_ylabel('Solid')

ax6.plot(Year1, Cement, 'o-r') #produzione di cemento
ax6.set_xlabel('Anni')
ax6.set_ylabel('Cement')

ax7.plot(Year1, GasFlaring, 'o-r') #combustione di gas
ax7.set_xlabel('Anni')
ax7.set_ylabel('GASFlaring')

ax8.plot(Year1, PerCapita, 'o-r') #pro capite
ax8.set_xlabel('Anni')
ax8.set_ylabel('PerCapita')

plt.show()