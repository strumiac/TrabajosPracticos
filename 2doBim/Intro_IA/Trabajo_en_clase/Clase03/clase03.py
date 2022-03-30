from cmath import nan
import pandas as pd
import numpy as np

df = pd.read_csv('clase3v2.csv', sep = ';', header = None)

# 1) Hallar z-score
media = np.nanmean(df, axis = 0)
std = np.nanstd(df, axis = 0)
df_zscore = (df - media)/std

# 2) Missing values con Pandas
print ('El dataset original tiene las siguientes dimensiones', df.shape)
print ('El dataset eliminando filas con NaN tiene las siguientes dimensiones'
        ,df.dropna(axis = 0).shape)
print ('El dataset eliminando columnas con NaN tiene las siguientes dimensiones'
        ,df.dropna(axis = 1).shape)
#    Missing values con Numpy
data_numpy = df.to_numpy()
ind = (np.argwhere(np.isnan(data_numpy)))
fil_ix = np.unique(ind[:,0])
col_ix = np.unique(ind[:,1])

drop_fil = np.delete(data_numpy, fil_ix, axis = 0)
drop_col = np.delete(data_numpy, col_ix, axis = 1)

# 3) Missing values reemplazo por media de la columna
print (data_numpy[ind[:,0],ind[:,1]])

def replace_NaN_media(df):
    data_numpy = df.to_numpy()
    ind = (np.argwhere(np.isnan(data_numpy)))
    data_numpy[ind] = 1000
    return data_numpy

#print(replace_NaN_media(df))