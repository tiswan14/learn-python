def kuadrat(angka):
    return angka**2


print(f"Hasil dari fungsi kuadrat {kuadrat(5)}")

# Dengan lambda
kuadrat = lambda angka: angka**2
print(f"Hasil dari lambda kuadrat {kuadrat(3)}")

pangkat = lambda num, pow: num**pow
print(f"Hasil dari lambda pangkat {pangkat(3, 3)}")

# Sortin untuk list biasa
data_list = ["ucup", "deden", "markonah"]
data_list.sort()
print(f"Hasil dari sort {data_list}")
data_list.sort(key=len)
print(f"Hasil dari sort pakai key panjang kata {data_list}")

# sort pakai lambda
data_list = ["otong", "ucup", "dudung"]

data_list.sort(key=lambda nama: len(nama))
print(f"Hasil dari sort pakai lambda {data_list}")

# Filter kasus genap
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def kurang_dari_lima(angka):
    return angka < 5 + 1


data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru_lambda = list(filter(lambda x: x < 5, data_angka))
print(data_angka_baru)
print(data_angka_baru_lambda)

data_genap = list(filter(lambda x: (x % 2 != 1), data_angka))
print(data_genap)
data_ganjil = list(filter(lambda x: (x % 2 == 1), data_angka))
print(data_ganjil)
data_kelipatan = list(filter(lambda x: (x % 3 == 0), data_angka))
print(data_kelipatan)


# Anonymous Funct
def pangkat(angka, n):
    hasil = angka**2
    return hasil


data_hasil = pangkat(5, 2)
print(f"pakai fungsi biasa {data_hasil}")

# dengan currying menjadi


def pangkat(n):
    return lambda angka: angka**n


pangkat2 = pangkat(2)
print(f"hasil dari pangkat2 {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"hasil dari pangkat2 {pangkat3(3)}")

print(f"Pangka bebas {pangkat(5)(5)}")
