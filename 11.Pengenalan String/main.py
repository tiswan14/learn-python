data = "Data ini adalah string"
print(data)
print(type(data))

# String bisa digunakan pakai single quote dan double qoute

data = '"Hallo apakabar?"'
print(data)

data = "'Hallo apakabar?'"
print(data)

data = "Ini hari jum'at"
print(data)

# Membuat tanda menjadi string
data = "Mari shalat jum'at"
print(data)

# Backslash
print("C:/User/Wannz")

# Tab
print("Tiswan\t\t\tKambing")

# Backspace
print("Kuntul \bdan \bsaja\n")

# NewLine
print("Baris pertama.\nBaris kedua.")  # LF > Linefit
print("Baris pertama.\rBaris kedua.")  # CR > Carriage return
print("Baris pertama.\r\nBaris kedua.")

# String literal atau raw
print("C:\new folder")  # akan salah pathnya

# Ini pakai raw string
print(r"C:\new folder")

# Merubah semua ke Uppercase
salam = "Bro!"
print("Normal    = " + salam)
salam = salam.upper()
print("Uppercase = " + salam)

# Merubah ke Lowercase
salam = salam.lower()
print("LowerCase = " + salam)

# Pengecekan dengan isX method
judul = "Pangandaran Bersemi Kembali"
cek_judul = judul.istitle()
print(judul + " Apakah ini judul = " + str(cek_judul))

# ngecek Komponen starswith
cek_start = "Tiswan saja".startswith("Tiswan")
print("Start = " + str(cek_start))

cek_end = "Tiswan saja".endswith("saja")
print("End   = " + str(cek_end))

# Penggabungan Komponen join() split()
pisah = ["aku", "sayang", "kamu"]
gabung = " ".join(pisah)
print(pisah)
print(gabung)
# split
gabung = "akuehmsayangehmkamu"
print(gabung.split("ehm"))

# Alokasi Karakter
kanan = "Kanan".rjust(10)
print("'" + kanan + "'")

kiri = "Kiri".ljust(10)
print("'" + kiri + "'")

tengah = "Tengah".center(20, "-")
print(tengah)

# Menghilangkan tanda strip()
tengah = tengah.strip("-")
print(tengah)
