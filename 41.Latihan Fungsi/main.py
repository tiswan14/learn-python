import os

# Program menghitung luas dan keliling persegi panjang
# os.system("clear")
# print(f"{'PROGRAM MEGHITUNG LUAS':^40}")
# print(f"{'KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40}")

# # Mengambil Input user
# LEBAR = int(input("Masukan nilai Lebar   = "))
# PANJANG = int(input("Masukan nilai Panjang = "))

# # Program Menghitung luasnya
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)

# # Tampilkan hasilnya


def header():
    os.system("clear")
    print(f"{'PROGRAM MEGHITUNG LUAS':^40}")
    print(f"{'KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40}")


def input_user():
    # Mengambil Input user
    lebar = int(input("Masukan nilai Lebar   = "))
    panjang = int(input("Masukan nilai Panjang = "))
    return lebar, panjang


def hitung_luas(lebar, panjang):
    return panjang * lebar


def hitung_keliling(lebar, panjang):
    return 2 * (panjang + lebar)


def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")


while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR, PANJANG)
    KELILING = hitung_keliling(LEBAR, PANJANG)
    opsi = input(
        "Pilih Program :\n1. Hitung Keliling\n2. Hitung Luas\n3. Keduanya\nAnda memilih No: "
    )
    if opsi == "1":
        display("Keliling", KELILING)
    elif opsi == "2":
        display("Luas", LUAS)
    elif opsi == "3":
        display("Keliling", KELILING)
        display("Luas", LUAS)
    else:
        print("Keyword yang anda masukan tidak ada! pilih (1/2/3) saja")

    isContinue = input("Apakah lanjut(y/n) : ")
    if isContinue == "n":
        break
print("Program selasai and babay")
