def kuadrat(input):
    hasil = input**2
    return hasil


y = kuadrat(5)
print(y)

z = 10 + kuadrat(1)
print(z)


def tambah(angka1, angka2):
    return angka1 + angka2


hasil = tambah(10, 5)
print(hasil)


def operasi_aritmatika(angka1, angka2):
    tambah = angka1 + angka2
    kali = angka1 * angka2
    kurang = angka1 - angka2
    bagi = angka1 / angka2

    return tambah, kali, bagi, kurang


k, l, m, n = operasi_aritmatika(10, 5)
print(f"Hasil + = {k}")
print(f"Hasil * = {l}")
print(f"Hasil - = {m}")
print(f"Hasil / = {n}")
