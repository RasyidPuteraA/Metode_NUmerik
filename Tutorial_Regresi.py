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

# Menghitung model regresi linear untuk Produksi
X = np.arange(1, 13).reshape(-1, 1)
y = produksi.flatten()

regressor = LinearRegression()
regressor.fit(X, y)
y_pred = regressor.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(np.arange(1, 13), y, color='blue', label='Data Observasi')
plt.plot(np.arange(1, 13), y_pred, color='red', linewidth=2, label='Model Regresi Linear')
plt.legend()
plt.xlabel('Bulan')
plt.ylabel('Produksi')
plt.title('Model Regresi Linear untuk Produksi')
plt.xticks(np.arange(1, 13), bulan, rotation=45)
plt.show()

# Menampilkan koefisien regresi linear dan intercept untuk Produksi
print('\nkoefisien Regresi Linear untuk Produksi:', regressor.coef_[0])
print('Intercept untuk Produksi:', regressor.intercept_)

# Menghitung model regresi linear untuk Terpasang
X = np.arange(1, 13).reshape(-1, 1)
y = terpasang.flatten()

regressor = LinearRegression()
regressor.fit(X, y)
y_pred = regressor.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(np.arange(1, 13), y, color='blue', label='Data Observasi')
plt.plot(np.arange(1, 13), y_pred, color='red', linewidth=2, label='Model Regresi Linear')
plt.legend()
plt.xlabel('Bulan')
plt.ylabel('Terpasang')
plt.title('Model Regresi Linear untuk Terpasang')
plt.xticks(np.arange(1, 13), bulan, rotation=45)
plt.show()

# Menampilkan koefisien regresi linear dan intercept untuk Terpasang
print('\nkoefisien Regresi Linear untuk Terpasang:', regressor.coef_[0])
print('Intercept untuk Terpasang:', regressor.intercept_)

# Menghitung model regresi linear untuk Terjual
X = np.arange(1, 13).reshape(-1, 1)
y = terjual.flatten()

regressor = LinearRegression()
regressor.fit(X, y)
y_pred = regressor.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(np.arange(1, 13), y, color='blue', label='Data Observasi')
plt.plot(np.arange(1, 13), y_pred, color='red', linewidth=2, label='Model Regresi Linear')
plt.legend()
plt.xlabel('Bulan')
plt.ylabel('Terjual')
plt.title('Model Regresi Linear untuk Terjual')
plt.xticks(np.arange(1, 13), bulan, rotation=45)
plt.show()

# Menampilkan koefisien regresi linear dan intercept untuk Terjual
print('\nkoefisien Regresi Linear untuk Terjual:', regressor.coef_[0])
print('Intercept untuk Terjual:', regressor.intercept_)

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

# Menampilkan koefisien regresi linear dan intercept untuk Susut
print('\nkoefisien Regresi Linear untuk Susut:', regressor.coef_[0])
print('Intercept untuk Susut:', regressor.intercept_)

