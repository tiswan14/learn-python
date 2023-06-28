import datetime

data_waktu = datetime.datetime.now()
print(f"Hari sekarang {data_waktu}")
print(f"Tahun sekarang {data_waktu.year}")
print(f"Bulan sekarang {data_waktu.month}")
print(f"Tanggal sekarang {data_waktu.day}")
print(f"Hari ini hari {data_waktu.strftime('%A')}")


from collections import Counter

data = ["a", "b", "c", "d", "a", "a", "a", "a"]

# Tidak pakai library
# counter = 0
# for i in data:
#     if i == "a":
#         counter += 1


# print(counter)

data_count = Counter(data)
print(f"Data Count   : {data_count}")

print(f"Data Count A : {data_count['a']}")


import io

file = io.open("wanz.txt", "r")

print(file.read())
