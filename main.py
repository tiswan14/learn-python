# Exception akan terjadi pada saat program mengalami error runtime
# Contoh sederhana untuk menangkap runtime error
from math import nan
import os

# input_user = int(input("Masukan angka : "))
# hasil = nan

# try:
#     hasil = 10 / input_user
# except:
#     print("Input tidak boleh 0")

# print(f"Hasilnya adalah = {hasil}")

# Contoh di aplikasi
os.system("clear")
while True:
    angka = int(input("Masukan angka pembagi = "))
    try:
        hasil = 10 / angka
        print(f"Hasil = {hasil}")
        is_done = input("Apalah lanjut(y/n): ")
        if is_done == "n":
            break
    except:
        print(f"Input anda {angka} tidak bisa di lakukan mamen")

print("Akhir dari program")

while True:
    try:
        with open("tampan.txt", "r") as file:
            print(file.read())
        break
    except:
        print(
            "Data tidak ditemukan dan saya akan membuatkan kamu file baru yang bernama itu terimakgajih haha"
        )
        with open("tampan.txt", "w", encoding="utf-8") as file:
            file.write("Hai ini file nya sudah jadi mamen")
        break

print("Terimakasih ini akhir dari program 2 ya mamen mamenkuh")
