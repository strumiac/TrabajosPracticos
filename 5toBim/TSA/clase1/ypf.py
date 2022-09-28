import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('YPFD.2000.2021.csv')

df = df.iloc[::-1]
df = df[df["ultimoPrecio"] > 0]
df['fecha'] = pd.to_datetime(df['fechaHora'], format = '%Y-%m-%d')


ticks_to_use = df['fecha'][::75]
labels = [i.strftime("%Y-%m-%d") for i in ticks_to_use]

plt.figure(figsize = (10,8))
plt.plot(df['fecha'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S')), df['ultimoPrecio'])
plt.gca().set_xticks(ticks_to_use.apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S')))
plt.gca().set_xticklabels(labels, rotation = 45, fontsize = 8)
plt.ylabel('Último precio', fontsize = 12)
plt.title('YPFD.2000.2021.csv', fontsize = 14)
plt.show()