data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()
print(f"Data 2D      : {data_2D}")
print(f"Data 2D Copy : {data_2D_copy}")


# Mengambil data kesatu
data = data_2D[1][0]
print(f"Data    : {data}")

# Address Semuanya
print(f"Address Data 2D Asli : {hex(id(data_2D))}")
print(f"Address Data 2D Copy : {hex(id(data_2D_copy))}")

# Address Member ke-1
print("Address member ke-1")
print(f"Address Data 2D Asli : {hex(id(data_2D[0]))}")
print(f"Address Data 2D Copy : {hex(id(data_2D_copy[0]))}")

# Berubah duaduanya
data_2D[0][0] = 10
print(f"Data 2D      : {data_2D}")
print(f"Data 2D Copy : {data_2D_copy}")

# Kita gunakan deepcopy
from copy import deepcopy

data_2D = [data_0, data_1, 11]
data2D_deepcopy = deepcopy(data_2D)

data_2D[0][0] = 9
print(f"Address Data 2D Asli : {hex(id(data_2D[0]))}")
print(f"Address Data 2D Deep : {hex(id(data2D_deepcopy[0]))}")

print(f"Data 2D      : {data_2D}")
print(f"Data 2D Deep : {data2D_deepcopy}")
