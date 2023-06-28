import datetime
import os
import string
import random

# Tempalate dict Mahasiswa
mahasiswa_tempalate = {
    "nama": "nama",
    "nim": 00000000,
    "sks_lulus": 0,
    "lahir": datetime.datetime(1111, 11, 11),
}

data_mahasiswa = {}
while True:
    os.system("clear")
    print(f"{'Selamat Datang':^20}")
    print(f"{'Data Masiswa':^20}")
    print("-" * 20)

    mahasiswa = dict.fromkeys(mahasiswa_tempalate.keys())

    mahasiswa["nama"] = input("Nama Mahasiwa : ")
    mahasiswa["nim"] = int(input("NIM Mahasiswa : "))
    mahasiswa["sks_lulus"] = int(input("SKS Lulus : "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir (1-31) : "))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = "".join((random.choice(string.ascii_uppercase) for i in range(3)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"{'KEY':<7} {'NIM':<10} {'Nama':<14} {'SKS':<6} {'Lahir':<5}")
    print("-" * 50)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]["nama"]
        NIM = data_mahasiswa[KEY]["nim"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
        print(f"{KEY:<7}{NIM:<6} {NAMA:<17} {SKS:<9} {LAHIR}")

    print("\n")
    print("-" * 50)

    is_done = input("Mau tambah lagi (y/n)? : ")
    if is_done == "n":
        break

print("Akhir dari program makacih")
