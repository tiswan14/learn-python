data_angka = [1, 5, 7, 11, 14, 15, 16, 5, 5, 5, 5, 4, 3, 3, 3, 3]
print(f"data_angka : \n{data_angka}")

# Count data
jumlah_data5 = data_angka.count(5)
jumlah_data3 = data_angka.count(3)

print(f"Jumlah angka 5 ada : {jumlah_data5}")
print(f"Jumlah angka 3 ada : {jumlah_data3}")

# Ambil Posisi Data
data = ["Ucup", "Mimin", "Suhli"]
print(f"Data : \n{data}")

index_ucup = data.index("Ucup")
print(f"Ucup index ke - {index_ucup}")

# Mengurutkan list
print(f"Data angka sebelum sort\n{data_angka}")
data_angka.sort()
print(f"Data angka sesudah di sort\n{data_angka}")

print(f"Data normal\n{data}")
data.sort()
print(f"Data sort\n{data}")

# Membalikan urutan list
data_angka.reverse()
data.reverse()

print(f"Data angka reverse\n{data_angka}")
print(f"Data reverse\n{data}")
