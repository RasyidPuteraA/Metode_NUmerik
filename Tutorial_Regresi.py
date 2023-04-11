import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Membaca data Excel ke dalam DataFrame
df = pd.read_excel('Data.xlsx')

# Mengambil data Produksi, Terpasang, Terjual, dan Susut dari DataFrame
produksi = np.array(df.loc[df['Unnamed: 0'] == 'Produksi'].iloc[:, 1:])
terpasang = np.array(df.loc[df['Unnamed: 0'] == 'Terpasang'].iloc[:, 1:])
terjual = np.array(df.loc[df['Unnamed: 0'] == 'Terjual'].iloc[:, 1:])
susut = np.array(df.loc[df['Unnamed: 0'] == 'Susut'].iloc[:, 1:])
bulan = df.columns[1:]

# Menghitung model regresi linear untuk Susut
X = np.arange(1, 13).reshape(-1, 1)
y = susut.flatten()

regressor = LinearRegression()
regressor.fit(X, y)
y_pred = regressor.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(np.arange(1, 13), y, color='blue', label='Data Observasi')
plt.plot(np.arange(1, 13), y_pred, color='red', linewidth=2, label='Model Regresi Linear')
plt.legend()
plt.xlabel('Bulan')
plt.ylabel('Susut')
plt.title('Model Regresi Linear untuk Susut')
plt.xticks(np.arange(1, 13), bulan, rotation=45)
plt.show()

# Menampilkan koefisien regresi linear (slope) dan intercept
print('Koefisien Regresi Linear (Slope):', regressor.coef_[0])
print('Intercept:', regressor.intercept_)
