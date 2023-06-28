data_angka = ()
jumlah_index = int(input("Masukan index : "))

for data in range(jumlah_index):
    data = input(f"Masukan data {data+1} = ")
    data_angka += (data,)

for i in data_angka:
    print(f"Data nya yang tadi di input : {i}")
