def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")


fungsi(nama="Eko", tinggi=170, berat=80)


def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")


fungsi(nama="Tiswan", tinggi=172, berat=85)


# Studi kasus
def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    return output


hasil_tambah = math(1, 2, 3, 4, 5, 6, 7, 8, 9, option="tambah")
hasil_kali = math(1, 2, 3, 4, option="kali")

print(hasil_tambah)
print(hasil_kali)
