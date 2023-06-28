teman = {"wan": "Tiswan sitampan", "tong": "Otong surotong", "dung": "Dudung surudung"}

# Looping first try

for temans in teman:  # Yang keluar adalah keynya
    print(temans)

# Operator untuk mengambil item/ iterable
keys = teman.keys()
print(keys)

for key in teman:
    print(teman.get(key))

values = teman.values()
print(values)

for value in teman.values():
    print(value)

items = teman.items()
print(items)

for item in teman.items():
    print(item)

for key, value in teman.items():
    print(f"key: {key}, value: {value}")
