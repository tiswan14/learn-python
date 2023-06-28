def hello_world(nama):
    print(f"Selamat datang wahai dunia {nama}")


hello_world("Tiswan saja")
hello_world("Sudiarjo")

# Tambah dengan menggunakan fungsi


def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_1
    print(f"{angka_1} + {angka_2} = {hasil}")


tambah(5, 5)
tambah(1, 3)


def say_hi(buah):
    data_buah = buah.copy()
    for buah in nama_buah:
        print(f"Ini adalah buah {buah}")


nama_buah = ["Jeruk", "Mangga", "Pear"]

say_hi(nama_buah)
