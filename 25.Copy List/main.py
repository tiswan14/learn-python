# Teknik Menduplikat List
a = ["Ucup", "Otong", "Dudung"]
print(f"Data a = {a}")
b = a
print(f"Data b = {b}")

a[1] = "Michael"
b.sort()
print(f"Data = {a}")
print(f"Data = {b}")

# Addres dari kedua list a dan b
print(f"Address a = {hex(id(a))}")
print(f"Address b = {hex(id(b))}")

# Menduplikat list dengan copy
print("Membuat list c dengan a.copy")
c = a.copy()
print(f"Address c = {hex(id(c))}")

print(f"Data a = {a}")
print(f"Data b = {b}")
print(f"Data c = {c}")

c[0] = "Dadang"
c.reverse()
print(f"Kita ubah data indek ke-0 : \n{c}")
