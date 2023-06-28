print(21 * "=")
print("Kalukalator Sederhana")
print(21 * "=")
angka_pertama = float(input("Masukan angka kesatu = "))
operator = input("Pilih operator (+, - , /, *) = ")
angka_kedua = float(input("Masukan angka kedua    = "))

if operator == "+":
    hasil = angka_pertama + angka_kedua
elif operator == "-":
    hasil = angka_pertama - angka_kedua
elif operator == "*":
    hasil = angka_pertama * angka_kedua
elif operator == "/":
    hasil = angka_pertama / angka_kedua
else:
    print("Operator tidak ada yang sesuai")

print(f"Hasil dari {int(angka_pertama)} {operator} {int(angka_kedua)} = {int(hasil)}")
