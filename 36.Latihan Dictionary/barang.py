import os
import string

barang_template = {
    "kode_barang": "kode_barang",
    "nama_barang": "nama_barang",
    "jumlah": "harga_barang",
}

data_barang = {}
while True:
    os.system("clear")
    print(f"{'Selamat Datang':^20}")
    print(f"{'Toko Subur Jaya':^20}")
    print("-" * 20)

    barang = dict.fromkeys(barang_template.keys())

    barang["kode_barang"] = input("Kode Barang : ")
    barang["nama_barang"] = input("Nama Barang : ")
    barang["jumlah"] = int(input("Masukan Jumlah : "))

    for barang in data_barang:
        kode = data_barang["kode_barang"]
        print(kode)
