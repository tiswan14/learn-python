# For loop
kumpulan_angka = [4, 2, 3, 5, 7, 1]
for angka in kumpulan_angka:
    print(f"Angka = {angka}")

kumpulan_peserta = ["Asep", "Dadang", "Markonah", "Balse"]
for peserta in kumpulan_peserta:
    print(f"Peserta = {peserta}")

# For loop dan range
print("For Loop")
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka pake for   = {kumpulan_angka[i]}")

# While Loop
print("While Loop")
i = 0
while i < panjang:
    print(f"Angka pake while = {kumpulan_angka[i]}")
    i += 1

# List comprehension
print("List comprehension")
data = ["Ucup", 1, 2, 3, "Zaran"]
[print(f"Data = {i}") for i in data]

# Enumerate
print("Enumerate")

data_list = ["Ucup", 1, 2, 3, "Zaran"]
for index, datas in enumerate(data_list):
    print(f"Index ke-{index}. Data = {datas}")

angka = [10, 5, 4, 7, 8, 9]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)
