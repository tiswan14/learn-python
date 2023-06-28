# Format String

# Contoh generic
nama = "Tiswan"
str = "Halo " + nama
format_str = f"Helo {nama}"
print(str)
print(format_str)

angka = 2002.2
format_str = f"Angka = {angka}"
print(format_str)

boolean = True
format_str = f"Bool  = {boolean}"
print(format_str)

bil_bulat = 20
format_str = f"Bil. Bulat = {bil_bulat:d}"
print(format_str)

ribuan = 50000
format_str = f"Ribuan = {ribuan:,}"
print(format_str)

ratusan = 500000
format_str = f"Ratusan = {ratusan:,}"
print(format_str)

# Decimal
angka = 2005.54321
format_str = f"Desimal = {angka:.1f}"
print(format_str)

# Leading zero atau kosong
format_str = f"Desimal = {angka:09.1f}"
print(format_str)

# Menampilkan tanda + atau -
angka_plus = 10.1234
angka_min = -10

format_plus = f"Angka plus = {angka_plus:+.2f}"
format_min = f"Angka min  = {angka_min:+d}"

print(format_plus)
print(format_min)

# Memformat persen
persen = 0.045
format_persen = f"Persen = {persen:.2%}"
print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"Total = {harga * jumlah:,}"
print(format_string)

# Format angka lain binary,octal,hexa
angka = 255
format_binary = f"Binary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hexa = f"Hexa = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexa)
