import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag

dane = pd.read_csv(r"sub-01_trial-05.csv", delimiter=',', engine='python')
czestosc_probkowania=200

t = np.linspace (0, 37.96, 200*37.96)
sygnal=dane["k2"]

filtr= ag.pasmowozaporowy(sygnal, czestosc_probkowania, 49,51 )
filtr2= ag.pasmowoprzepustowy(filtr, czestosc_probkowania, 1, 50)

plt.plot(sygnal) #Rycina 1. Wykresy sygnału przed filtracją.
plt.plot(filtr2) #Rycina 2. Wykresy sygnału po filtracji.
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
