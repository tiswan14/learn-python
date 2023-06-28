a = ()
b = int(input("Masukan data  : "))

print()
for i in range(b):
    element = int(input("Masukan angka : "))
    a = a + (element,)

for i in a:
    print(f"Data angka yang kita input tadi = {i}")
