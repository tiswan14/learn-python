import sains.matematika

# from sains import fisika
from sains.fisika import gaya

hasil_tambah = sains.matematika.tambah(1, 2, 3, 4, 5)
print(f"Hasil tambah dari package sains = {hasil_tambah}")

hasil_fisika = gaya(2, 3)
print(f"Hasil fisika = {hasil_fisika}")
