# Memasukan data argument
import os

os.system("clear")


def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")


fungsi("Tiswan", 171, 56)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")


fungsi(["Bambang", 176, 40])


# Kenalan dengan args
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")


fungsi("Dudung", 150, 55)


# Studi kasus
def tambah(*data):
    # dapat di iterasi kalau pake args
    output = 0
    for angka in data:
        output += angka
    return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"hasil dari = {hasil}")

hasil = tambah(9, 10)
print(f"hasil = {hasil}")
