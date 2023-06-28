data_nama = "Tiswan"
data_umur = 20
data_tinggi = 171.3
data_nomor_sepatu = 42


# String Normal
data_string = f"Nama = {data_nama}, Umur = {data_umur}, TB = {data_tinggi}, No. Sepatu = {data_nomor_sepatu}."

print(5 * "=" + "Data String" + 5 * "=")
print(data_string)

# String Multiline
data_string = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTB = {data_tinggi}, \nNo. Sepatu = {data_nomor_sepatu}."

print("\n\n" + 5 * "=" + "Data String" + 5 * "=")
print(data_string)

# String Multiline Strip Triplets
data_string = f"""
Nama       = {data_nama:>6}
Umur       = {data_umur:>6}
Tinggi     = {data_tinggi:>6}
No. Sepatu = {data_nomor_sepatu:>6}
"""

print(5 * "=" + "Data String" + 5 * "=")
print(data_string)
