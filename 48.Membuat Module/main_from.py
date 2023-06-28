# Module matematika
from matematika import (
    tambah as add,
    kali,
    pangkat,
)  # /Mengambil beberap module dan alias
from matematika import *  # Mengambil semua ->Tidak direkomendasikan karena kita tau module apa yang kita akan ambil
import matematika as math  # mengaliaskan atau bisa manggil math juga tida akan error karena di aliaskan

hasil_tambah = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Hasil tambah    : {hasil_tambah}")

hasil_kali = kali(1, 2, 3, 4, 5)
print(f"Hasil perkalian : {hasil_kali}")

hasil_pangkat3 = pangkat(3)
print(f"Hasil pangkat 3 : {hasil_pangkat3(3)}")
