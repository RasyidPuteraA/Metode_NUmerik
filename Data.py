import numpy as np

# contoh data yang akan di gunakan

#SOAL A-B
#Versi Komplit
A = np.array([[2, 8, 6, 20], [4, 2, -2, -2], [3, -2, 1, 12]], dtype=float)

#Versi Parsial X
a = np.array([[2, 8, 6], [4, 2, -2], [3, -2, 1]], dtype=float)
b = np.array([20, -2, 12], dtype=float)

#SOAL C-D
#Versi Komplit
C = np.array([[10, -1, 2, 0, 6], [-1, 11, -1, 3, 25], [2, -1, 10, -1, -11], [0, 3, -1, 8, 15]], dtype=float)

#Versi Parsial
c = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]], dtype=float)
d = np.array([6, 25, -11, 15], dtype=float)