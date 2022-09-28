import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('catfish.csv')


ticks_to_use = df['Date'][::10]

plt.plot(df['Date'], df['Total'])
plt.gca().set_xticks(ticks_to_use)
plt.gca().set_xticklabels(ticks_to_use, rotation = 45, fontsize = 8 )
plt.ylabel('Total', fontsize = 12)
plt.title('catfish.csv', fontsize = 14)
plt.show()