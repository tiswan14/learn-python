def say_hello(nama="Tiswan"):
    print(f"Hallo bos {nama}")


say_hello()
say_hello("Brody")


def sapa(nama="Kamu", pesan="Assalamu'alaikum"):
    print(f"Hai bos {nama}, {pesan}")


sapa("Tiswan", "Lagi ngapain nich?")
sapa("Otong")
sapa()


def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil


print(hitung_pangkat(10, 3))

# Mengakses pakai argumen

hasil = hitung_pangkat(pangkat=2, angka=5)
print(hasil)


def fungsi(angka1=1, angka2=2, angka3=3, angka4=4):
    hasil = angka1 + angka2 + angka3 + angka4
    return hasil


print(fungsi())
print(fungsi(angka1=10))
