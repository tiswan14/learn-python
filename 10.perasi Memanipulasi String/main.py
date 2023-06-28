# 1. Menyambung Sting (Concacenate)
nama_pertama = "Tiswan"
nama_tengah = "D"
nama_akhir = "Boys"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung Panjang String
panjang = len(nama_lengkap)
print("Panjang nama : " + nama_lengkap + " adalah : " + str(panjang))

# 3. Operator Untuk String
# Mengecek apakah ada komponen char atau string di string
d = "T"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

# Mengulang String
print(10 * "wk")
print("wk" * 20)

# Indexing String
print("Index ke - 0 : " + nama_lengkap[0])
print("Index ke - 1 : " + nama_lengkap[1])
print("Index ke - (-1) : " + nama_lengkap[-1])
print("Index ke - (-2) : " + nama_lengkap[-2])
print("Index ke - (-3) : " + nama_lengkap[-3])
print("Index ke - (-3) : " + nama_lengkap[-4])
print("Index ke - (0:5) : " + nama_lengkap[0:6])
print("Index ke - (0:12:2) : " + nama_lengkap[0:12:2])

# item paling besar
print("Item paling besar : " + max(nama_lengkap))
# item paling kecil
print("Item paling kecil : " + min(nama_lengkap))

# 4. Operator dalam bentuk method
data = "otong surotor parontong"
jumlah = data.count("o")
print("Banyak huruf o pada " + data + " adalah : " + str(jumlah))
