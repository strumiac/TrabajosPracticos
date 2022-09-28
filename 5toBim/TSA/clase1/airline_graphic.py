import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('airline-passengers.csv')


ticks_to_use = df['Month'][::6]

plt.plot(df['Month'], df['Passengers'])
plt.gca().set_xticks(ticks_to_use)
plt.gca().set_xticklabels(ticks_to_use, rotation = 90)
plt.ylabel('Passengers', fontsize = 12)
plt.title('airline-passengers.csv', fontsize = 14)
plt.show()