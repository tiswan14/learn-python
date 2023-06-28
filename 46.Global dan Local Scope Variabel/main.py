import os

os.system("clear")
nama_global = "otong"  # Ini variabel global dimana kita akses di dalam fungsi


def fungsi():
    print(f"nama = {nama_global}")


fungsi()

# Akses variabel global dalam loop
for i in range(1, 5 + 1):
    print(f"Hai {nama_global} {i}")

if True:
    print(f"Nama saya adalah {nama_global}")


##Variabel lokal scope
def fungsi2():
    nama_local = "ucup"  # -> Variabel lokal scope


fungsi2()
# print(nama_local) Tidak bisa di lakukan


# contoh penggunaan 1
def say_otong():
    print(f"hay nama saya {nama}")


nama = "otong"  # Error jika variabel ada di bawah fungsi
say_otong()

# contoh penggunaan 2 :merubah variabel global
angka = 0
name = "ucup"


def ubah(nilai_baru, nama_baru):
    global angka  # Fungsi ini mendapat akses jadi variabel global
    global name
    angka = nilai_baru
    name = nama_baru


print(f"Sebelum di ubah : {angka, name}")
ubah(10, "otong")
print(f"Sesudah di ubah : {angka,name}")

# contoh 3

angka = 0
for i in range(1, 5):
    angka += 1
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)
