# (0)/(-3)  (1)/(-2)  (2)/(-1)
data = ["Ucup", "Otong", "Dudung", "Mirna"]

# Mengambil data dari list
data_pertama = data[0]
print(f"data_pertama  : {data_pertama}")
data_terakhir = data[2]
print(f"data_terakhir : {data_terakhir}")
data_ucup = data[-3]
print(f"data_ucup     : {data_ucup}")

# Mengambil info jumlah data dalam List
panjang_data = len(data)
print(f"Panjang data  : {panjang_data}")

# Manipulasi Data List

# Menambahkan data list sesuai posisi
print(f"Data sebelum ditambah : \n{data}")
data.insert(0, "Asep baskom")
print(f"Data sesudah ditambah : \n{data}")

# Menambah di akhir di list
data.append("Jajang")
print(f"Data sesudah ditambah  : \n{data}")

# Menambah list dengan list
data_baru = ["Ujang", "Usep", "Markonah"]
data.extend(data_baru)
print(f"Data sesudah di extend : \n{data}")

# Merubah data

data[0] = "Asep Sleding"
print(f"Rename data : \n{data}")

# Meremove data
data.remove("Markonah")
print(f"Setelah di remove : {data}")

# Meremove data paling belakang
data.pop()
print(f"Data akhir akan teremove : \n{data}")
