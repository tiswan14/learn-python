data_0 = [1, 2]
data_1 = [3, 4]

list_biasa = [1, 2, 3, 4]

print(f"Data list biasa : {list_biasa}")

list_2d = [data_0, data_1, list_biasa, 6, 7]
print(f"List 2D : {list_2d}")

# Contoh Penggunaan
peserta_0 = ["Ucup", 25, "Lak-laki"]
peserta_1 = ["Otong", 16, "Laki-laki"]
peserta_2 = ["Mindah", 22, "Perempuan"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"List Peserta : {list_peserta}\n\n")

for peserta in list_peserta:
    print(f"Nama : {peserta[0]}")
    print(f"Umur : {peserta[1]} tahun")
    print(f"Jk   : {peserta[2]}\n")

list_perserta_copy = list_peserta.copy()
list_peserta[0] = "Michael"
print(f"Peserta : {list_perserta_copy}")
