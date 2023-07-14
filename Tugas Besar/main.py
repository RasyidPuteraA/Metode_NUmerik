# -*- coding: utf-8 -*-
"""Tugas_Besar_KEL_14.ipynb
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from datetime import timedelta

from sklearn.linear_model import LinearRegression
from google.colab import drive
drive.mount('/content/drive')

dataset = '/content/drive/MyDrive/TUGAS_BESAR'

df = pd.read_csv(os.path.join(dataset, '2019Floor7.csv'),
                 index_col="Date", parse_dates= True)

df.head()

df.dtypes

df.describe()

df.isna().sum()

"""#Filter Data yang Tidak Digunakan"""

df_fillter = df.filter(like='(degC)')
df = df.drop(columns=df_fillter.columns)

df_fillter = df.filter(like='(RH%)')
df = df.drop(columns=df_fillter.columns)

df_fillter = df.filter(like='(lux)')
df = df.drop(columns=df_fillter.columns)

df

"""#Mencari Data Kosong
- Maret
- Oktober
- Desember
"""

null_03 = df.loc["2019-03-1":"2019-03-31"].isnull().sum()
null_10 = df.loc["2019-10-1":"2019-10-30"].isnull().sum()
null_12 = df.loc["2019-12-1":"2019-12-30"].isnull().sum()

print(null_03)
print("\n\n")
print(null_10)
print("\n\n")
print(null_12)

"""#Interpolasi
  interpolasi pchip digunakan untuk mengisi atau mengganti nilai yang hilang atau tidak valid dalam suatu data dengan memperkirakan nilai-nilai tersebut berdasarkan polinomial kubik yang terdefinisi secara berpotongan
"""

di = df.interpolate(method='pchip')

di.loc["2019-01-01 00:00:00":"2019-12-31 23:59:00"]

"""#Cek Data Kosong Kembali
  Memastikan tidak ada data ynag masih kosong
"""

null_03 = di.loc["2019-03-1":"2019-03-31"].isnull().sum()
null_10 = di.loc["2019-10-1":"2019-10-30"].isnull().sum()
null_12 = di.loc["2019-12-1":"2019-12-30"].isnull().sum()


print(null_03)
print("\n\n")
print(null_10)
print("\n\n")
print(null_12)

"""#Konversi KWH"""

df_kwh = pd.DataFrame()

for i in range(17):
    df_kwh[di.columns[i]]= di[di.columns[i]]/60

df_kwh = df_kwh.rename(columns=lambda x: x.replace('(kW)', '(KWH)'))

df_kwh

"""#Olah Data Bulan
- Maret
- Oktober
- Desember

#WBP dan NON-WBP
"""

WBP_03  = 0
NWBP_03 = 0

for x in range(31):
    WBP_03  += df_kwh.loc[f"2019-03-{1+x} 17:00:00":f"2019-03-{1+x} 22:00:00"].sum().sum()
    NWBP_03 += df_kwh.loc[f"2019-03-{1+x} 22:01:00":f"2019-03-{1+x} 23:59:00"].sum().sum()
    NWBP_03 += df_kwh.loc[f"2019-03-{1+x} 00:00:00":f"2019-03-{1+x} 16:59:00"].sum().sum()

tb_03 = 972*((1.3*WBP_03)+NWBP_03)
print(f"WBP_03 \t\t\t = {WBP_03} kWH")
print(f"NWBP_03 \t\t = {NWBP_03} kWH")
print(f"Total Biaya Bln 3\t = Rp {tb_03:,.2f}\n\n")

d_WBP_03  = []
d_NWBP_03 = []

for x in range(31):
    d_WBP_03.append(df_kwh.loc[f"2019-03-{1+x} 17:00:00":f"2019-03-{1+x} 22:00:00"].sum().sum())
    d_NWBP_03.append(df_kwh.loc[f"2019-03-{1+x} 22:01:00":f"2019-03-{1+x} 23:59:00"].sum().sum() + df_kwh.loc[f"2019-03-{1+x} 00:00:00":f"2019-03-{1+x} 16:59:00"].sum().sum())

num3 = np.array(d_WBP_03)
dt_03 = pd.DataFrame(num3,columns=['Day_WBP'])

dt_03['Day_NWBP'] = d_NWBP_03
dt_03['Total'] = np.array(d_NWBP_03) + np.array(d_WBP_03)

dt_03.head()

WBP_10  = 0
NWBP_10 = 0

for x in range(31):
    WBP_10  += df_kwh.loc[f"2019-10-{1+x} 17:00:00":f"2019-10-{1+x} 22:00:00"].sum().sum()
    NWBP_10 += df_kwh.loc[f"2019-10-{1+x} 22:01:00":f"2019-10-{1+x} 23:59:00"].sum().sum()
    NWBP_10 += df_kwh.loc[f"2019-10-{1+x} 00:00:00":f"2019-10-{1+x} 16:59:00"].sum().sum()

tb_10 = 972*((1.3*WBP_10)+NWBP_10)
print(f"WBP_10 \t\t\t = {WBP_10} kWH")
print(f"NWBP_10 \t\t = {NWBP_10} kWH")
print(f"Total Biaya Bln 10 \t = Rp {tb_10:,.2f}\n\n")

d_WBP_10  = []
d_NWBP_10 = []

for x in range(31):
    d_WBP_10.append(df_kwh.loc[f"2019-10-{1+x} 17:00:00":f"2019-10-{1+x} 22:00:00"].sum().sum())
    d_NWBP_10.append(df_kwh.loc[f"2019-10-{1+x} 22:01:00":f"2019-10-{1+x} 23:59:00"].sum().sum() + df_kwh.loc[f"2019-10-{1+x} 00:00:00":f"2019-10-{1+x} 16:59:00"].sum().sum())

num10 = np.array(d_WBP_10)
dt_10 = pd.DataFrame(num10,columns=['Day_WBP'])

dt_10['Day_NWBP'] = d_NWBP_10

dt_10['Total'] = np.array(d_NWBP_10) + np.array(d_WBP_10)

dt_10.head()

WBP_12  = 0
NWBP_12 = 0

for x in range(31):
    WBP_12  += df_kwh.loc[f"2019-12-{1+x} 17:00:00":f"2019-12-{1+x} 22:00:00"].sum().sum()
    NWBP_12 += df_kwh.loc[f"2019-12-{1+x} 22:01:00":f"2019-12-{1+x} 23:59:00"].sum().sum()
    NWBP_12 += df_kwh.loc[f"2019-12-{1+x} 00:00:00":f"2019-12-{1+x} 16:59:00"].sum().sum()

tb_12 = 972*((1.3*WBP_12)+NWBP_12)
print(f"WBP_12 \t\t\t = {WBP_12} kWH")
print(f"NWBP_12 \t\t = {NWBP_12} kWH")
print(f"Total Biaya Bln 12 \t = Rp {tb_12:,.2f}\n\n")

d_WBP_12  = []
d_NWBP_12 = []

for x in range(31):
    d_WBP_12.append(df_kwh.loc[f"2019-12-{1+x} 17:00:00":f"2019-12-{1+x} 22:00:00"].sum().sum())
    d_NWBP_12.append(df_kwh.loc[f"2019-12-{1+x} 22:01:00":f"2019-12-{1+x} 23:59:00"].sum().sum() + df_kwh.loc[f"2019-12-{1+x} 00:00:00":f"2019-12-{1+x} 16:59:00"].sum().sum())

num12 = np.array(d_WBP_12)
dt_12 = pd.DataFrame(num12,columns=['Day_WBP'])

dt_12['Day_NWBP'] = d_NWBP_12

dt_12['Total'] = np.array(d_NWBP_12) + np.array(d_WBP_12)

dt_12.head()

"""#Assembly Tabel

"""

dh = pd.concat([dt_03, dt_10, dt_12],ignore_index=True)

dh.index +=1

dh

"""#Export Perubahan Tabel"""

datasave = '/content/drive/MyDrive/TUGAS_BESAR'
dh.to_csv(os.path.join(datasave, 'data_terbaru.csv'))

"""#Coba Tampilan Grafik"""

plt.scatter(dh.index, dh.Day_WBP)

plt.xlabel('Hari', fontsize=20)
plt.ylabel('WBP/Day', fontsize=20)
plt.show()

X1 = dh.index.values.reshape(-1,1)
y1 = dh.Day_WBP.values.reshape(-1,1)

reg = LinearRegression().fit(X1, y1)


print(f"\n\nscore regression = {reg.score(X1,y1)}\n")

print(reg.coef_)
print(reg.intercept_)

plt.scatter(dh.index,dh.Day_NWBP)

plt.xlabel('Hari', fontsize=20)
plt.ylabel('NWBP/Day', fontsize=20)
plt.show()


X1 = dh.index.values.reshape(-1,1)
y1 = dh.Day_NWBP.values.reshape(-1,1)

reg = LinearRegression().fit(X1, y1)


print(f"\n\nscore regression = {reg.score(X1,y1)}\n")

print(reg.coef_)
print(reg.intercept_)

"""#Interpolasi Lagrange"""

df

dl = df

dl.tail()

dl.describe()

print(dl.isnull().sum())

null_03 = dl.loc["2019-03-1":"2019-03-31"].isnull().sum()
null_10 = dl.loc["2019-10-1":"2019-10-30"].isnull().sum()
null_12 = dl.loc["2019-12-1":"2019-12-30"].isnull().sum()

print(null_03)
print("\n\n")
print(null_10)
print("\n\n")
print(null_12)

null_03_ = dl.loc["2019-03-1":"2019-03-31"]
null_10_ = dl.loc["2019-10-1":"2019-10-30"]
null_12_ = dl.loc["2019-12-1":"2019-12-30"]


rows1 = null_03_[null_03_.isna().any(axis=1)]
print(rows1)

rows2 = null_10_[null_10_.isna().any(axis=1)]
print(rows2)

rows3 = null_12_[null_12_.isna().any(axis=1)]
print(rows3)

#metode interpolasi Lagrange
for m in range(11):

    if m!=2:

        selected_rows = rows1[rows1[dl.columns[m]].isnull()]
        dff=selected_rows[dl.columns[m]]

        x=[1,2]
        y=[]

        for l in range(len(dff)):
            interpolasi3 = dl.loc[dff.index[l]-timedelta(minutes=2):dff.index[l]]
            for n in range(len(x)):
                y.append(interpolasi3[dl.columns[m]][n])

            xp=3
            yp=0

            for i in range(len(x)):
                p = 1
                for j in range(len(x)):
                    if i != j:
                        p = p * (xp - x[j])/(x[i] - x[j])
                yp = yp + p * y[i]

            dl.loc[dff.index[l],dl.columns[m]]=yp
            y.pop(0)
            y.pop(0)




            print(' Nilai interpolasi di %i adalah %.3f.' % (l, yp))

"""#Coba Pilih Interpolasi pada "z2_AC1(kW)"
"""

selected_rows = rows1[rows1['z2_AC1(kW)'].isnull()]
dff=selected_rows["z2_AC1(kW)"]

x=[1,2]
y=[]

for l in range(len(dff)):
    interpolasi3 = dl.loc[dff.index[l]-timedelta(minutes=2):dff.index[l]]
    for n in range(len(x)):
        y.append(interpolasi3["z2_AC1(kW)"][n])



    xp=3
    yp=0

    for i in range(2):
        p = 1
        for j in range(2):
            if i != j:
                p = p * (xp - x[j])/(x[i] - x[j])
        yp = yp + p * y[i]

    dl.loc[dff.index[l],"z2_AC1(kW)"]=yp
    y.pop(0)
    y.pop(0)




    print(' Nilai interpolasi di %i adalah %.3f.' % (l, yp))

for m in range(11):

        selected_rows = rows2[rows2[dl.columns[m]].isnull()]
        dff=selected_rows[dl.columns[m]]

        x=[1,2]
        y=[]

        for l in range(len(dff)):
            interpolasi10 = dl.loc[dff.index[l]-timedelta(minutes=2):dff.index[l]]
            for n in range(len(x)):
                y.append(interpolasi10[dl.columns[m]][n])

            xp=3
            yp=0

            for i in range(len(x)):
                p = 1
                for j in range(len(x)):
                    if i != j:
                        p = p * (xp - x[j])/(x[i] - x[j])
                yp = yp + p * y[i]

            dl.loc[dff.index[l],df.columns[m]]=yp
            for n in range(len(x)):
                y.pop(0)





            print(' Nilai interpolasi di %i adalah %.3f.' % (l, yp))

for m in range(11):

        selected_rows = rows3[rows3[dl.columns[m]].isnull()]
        dff=selected_rows[dl.columns[m]]

        x=[1,2]
        y=[]

        for l in range(len(dff)):
            interpolasi12 = dl.loc[dff.index[l]-timedelta(minutes=2):dff.index[l]]
            for n in range(len(x)):
                y.append(interpolasi12[dl.columns[m]][n])

            xp=3
            yp=0

            for i in range(len(x)):
                p = 1
                for j in range(len(x)):
                    if i != j:
                        p = p * (xp - x[j])/(x[i] - x[j])
                yp = yp + p * y[i]

            dl.loc[dff.index[l],dl.columns[m]]=yp
            y.pop(0)
            y.pop(0)




            print(' Nilai interpolasi di %i adalah %.3f.' % (l, yp))

"""#cek apakah ada nilai negatif pada dataframe"""

(dl < 0).sum().sum()

"""#Konvert KWH"""

dl_kwh = pd.DataFrame()

for i in range(17):
    dl_kwh[dl.columns[i]]= dl[dl.columns[i]]/60

dl_kwh = dl_kwh.rename(columns=lambda x: x.replace('(kW)', '(KWH)'))

dl_kwh

"""#Olah Data Bulan
- Maret
- Oktober
- Desember

#WBP dan NON-WBP
"""

WBPl_03  = 0
NWBPl_03 = 0

for x in range(31):
    WBPl_03  += dl_kwh.loc[f"2019-03-{1+x} 17:00:00":f"2019-03-{1+x} 22:00:00"].sum().sum()
    NWBPl_03 += dl_kwh.loc[f"2019-03-{1+x} 22:01:00":f"2019-03-{1+x} 23:59:00"].sum().sum()
    NWBPl_03 += dl_kwh.loc[f"2019-03-{1+x} 00:00:00":f"2019-03-{1+x} 16:59:00"].sum().sum()

tbl_03 = 972*((1.3*WBPl_03)+NWBPl_03)
print(f"WBPl_03 \t\t\t = {WBPl_03} kWH")
print(f"NWBPl_03 \t\t\t = {NWBPl_03} kWH")
print(f"Total Biaya Bln 3 (Lagrange)\t = Rp {tbl_03:,.2f}\n\n")

d_WBPl_03  = []
d_NWBPl_03 = []

for x in range(31):
    d_WBPl_03.append(dl_kwh.loc[f"2019-03-{1+x} 17:00:00":f"2019-03-{1+x} 22:00:00"].sum().sum())
    d_NWBPl_03.append(dl_kwh.loc[f"2019-03-{1+x} 22:01:00":f"2019-03-{1+x} 23:59:00"].sum().sum() + dl_kwh.loc[f"2019-03-{1+x} 00:00:00":f"2019-03-{1+x} 16:59:00"].sum().sum())

numl3 = np.array(d_WBPl_03)
dtl_03 = pd.DataFrame(numl3,columns=['Day_WBPl'])

dtl_03['Day_NWBPl'] = d_NWBPl_03
dtl_03['Total (Lagrange)'] = np.array(d_NWBPl_03) + np.array(d_WBPl_03)

dtl_03.head()

WBPl_10  = 0
NWBPl_10 = 0

for x in range(31):
    WBPl_10  += dl_kwh.loc[f"2019-10-{1+x} 17:00:00":f"2019-10-{1+x} 22:00:00"].sum().sum()
    NWBPl_10 += dl_kwh.loc[f"2019-10-{1+x} 22:01:00":f"2019-10-{1+x} 23:59:00"].sum().sum()
    NWBPl_10 += dl_kwh.loc[f"2019-10-{1+x} 00:00:00":f"2019-10-{1+x} 16:59:00"].sum().sum()

tbl_10 = 972*((1.3*WBPl_10)+NWBPl_10)
print(f"WBPl_10 \t\t\t = {WBPl_10} kWH")
print(f"NWBPl_10 \t\t\t = {NWBPl_10} kWH")
print(f"Total Biaya Bln 10 (Lagrange)\t = Rp {tbl_10:,.2f}\n\n")

d_WBPl_10  = []
d_NWBPl_10 = []

for x in range(31):
    d_WBPl_10.append(dl_kwh.loc[f"2019-10-{1+x} 17:00:00":f"2019-10-{1+x} 22:00:00"].sum().sum())
    d_NWBPl_10.append(dl_kwh.loc[f"2019-10-{1+x} 22:01:00":f"2019-10-{1+x} 23:59:00"].sum().sum() + dl_kwh.loc[f"2019-10-{1+x} 00:00:00":f"2019-10-{1+x} 16:59:00"].sum().sum())

numl10 = np.array(d_WBPl_10)
dtl_10 = pd.DataFrame(numl10,columns=['Day_WBPl'])

dtl_10['Day_NWBPl'] = d_NWBPl_10

dtl_10['Total (Lagrange)'] = np.array(d_NWBPl_10) + np.array(d_WBPl_10)

dtl_10.head()

WBPl_12  = 0
NWBPl_12 = 0

for x in range(31):
    WBPl_12  += dl_kwh.loc[f"2019-12-{1+x} 17:00:00":f"2019-12-{1+x} 22:00:00"].sum().sum()
    NWBPl_12 += dl_kwh.loc[f"2019-12-{1+x} 22:01:00":f"2019-12-{1+x} 23:59:00"].sum().sum()
    NWBPl_12 += dl_kwh.loc[f"2019-12-{1+x} 00:00:00":f"2019-12-{1+x} 16:59:00"].sum().sum()

tbl_12 = 972*((1.3*WBPl_12)+NWBPl_12)
print(f"WBPl_12 \t\t\t = {WBPl_12} kWH")
print(f"NWBPl_12 \t\t\t = {NWBPl_12} kWH")
print(f"Total Biaya Bln 12 (Lagrange)\t = Rp {tbl_12:,.2f}\n\n")

d_WBPl_12  = []
d_NWBPl_12 = []

for x in range(31):
    d_WBPl_12.append(dl_kwh.loc[f"2019-12-{1+x} 17:00:00":f"2019-12-{1+x} 22:00:00"].sum().sum())
    d_NWBPl_12.append(dl_kwh.loc[f"2019-12-{1+x} 22:01:00":f"2019-12-{1+x} 23:59:00"].sum().sum() + dl_kwh.loc[f"2019-12-{1+x} 00:00:00":f"2019-12-{1+x} 16:59:00"].sum().sum())

numl12 = np.array(d_WBPl_12)
dtl_12 = pd.DataFrame(numl12,columns=['Day_WBPl'])

dtl_12['Day_NWBPl'] = d_NWBPl_12

dtl_12['Total (Lagrange)'] = np.array(d_NWBPl_12) + np.array(d_WBPl_12)

dtl_12.head()

"""#Assembly Tabel

"""

dhl = pd.concat([dtl_03, dtl_10, dtl_12],ignore_index=True)

dhl.index +=1

dhl

datasave = '/content/drive/MyDrive/TUGAS_BESAR'
dh.to_csv(os.path.join(datasave, 'data_terbaru(Lagrange).csv'))

"""#Coba Tampilan Grafik"""

plt.scatter(dhl.index, dhl.Day_WBPl)

plt.xlabel('Hari', fontsize=20)
plt.ylabel('WBP (Lagrange)/Day', fontsize=20)
plt.show()

X1 = dhl.index.values.reshape(-1,1)
y1 = dhl.Day_WBPl.values.reshape(-1,1)

regl1 = LinearRegression().fit(X1, y1)


print(f"\n\nscore regression = {regl1.score(X1,y1)}\n")

print(regl1.coef_)
print(regl1.intercept_)

plt.scatter(dhl.index,dhl.Day_NWBPl)

plt.xlabel('Hari', fontsize=20)
plt.ylabel('NWBP (Lagrange)/Day', fontsize=20)
plt.show()


X1 = dhl.index.values.reshape(-1,1)
y1 = dhl.Day_NWBPl.values.reshape(-1,1)

regl2 = LinearRegression().fit(X1, y1)


print(f"\n\nscore regression = {regl2.score(X1,y1)}\n")

print(regl2.coef_)
print(regl2.intercept_)

"""#Prediksi Bulan Selanjutnya
- Nilai Rasio 3 Bln
- Interpolation Lagrange
"""

du = pd.DataFrame()

du['T_WBP'] = (dt_03.Day_WBP + dt_10.Day_WBP + dt_12.Day_WBP)/3

du['T_NWBP'] = (dt_03.Day_NWBP + dt_10.Day_NWBP + dt_12.Day_NWBP)/3

du['T_Day'] = du.T_WBP + du.T_NWBP

du.index +=1

du.dropna(inplace=True)


d1= (dt_03.loc[dt_03.index[30],'Day_WBP'] + dt_12.loc[dt_12.index[30],'Day_WBP'])/2
d2 = (dt_03.loc[dt_03.index[30],'Day_NWBP'] + dt_12.loc[dt_12.index[30],'Day_NWBP'])/2
d3 = d1 + d2



du.loc[-1]=[d1,d2,d3]
du.index = du.index + 1
du = du.sort_index()

print(du)

TEB = 972*(1.3*du.T_WBP.sum()+du.T_NWBP.sum())
print(f"\n\nTotal Estimasi Biaya = Rp{TEB:,.2f}\n")

dul = pd.DataFrame()

dul['T_WBPl'] = (dtl_03.Day_WBPl + dtl_10.Day_WBPl + dtl_12.Day_WBPl)/3

dul['T_NWBPl'] = (dtl_03.Day_NWBPl + dtl_10.Day_NWBPl + dtl_12.Day_NWBPl)/3

dul['T_Day (Lagrange)'] = dul.T_WBPl + dul.T_NWBPl

dul.index +=1

dul.dropna(inplace=True)


dl1= (dtl_03.loc[dtl_03.index[30],'Day_WBPl'] + dtl_12.loc[dtl_12.index[30],'Day_WBPl'])/2
dl2 = (dtl_03.loc[dtl_03.index[30],'Day_NWBPl'] + dtl_12.loc[dtl_12.index[30],'Day_NWBPl'])/2
dl3 = dl1 + dl2



dul.loc[-1]=[dl1,dl2,dl3]
dul.index = dul.index + 1
dul = dul.sort_index()

print(dul)

TEBl = 972*(1.3*dul.T_WBPl.sum()+dul.T_NWBPl.sum())
print(f"\n\nTotal Estimasi Biaya (Lagrange) = Rp{TEB:,.2f}\n")