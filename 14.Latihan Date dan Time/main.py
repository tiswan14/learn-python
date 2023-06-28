import datetime as dt

print("Silahkan Masukan Tanggal, \nBulan, dan Tahun lahir anda")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan \t: "))
tahun = int(input("Tahun \t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari lahirnya adalah      : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_bulan = (umur_hari.days % 365) // 30
umur_tahun = umur_hari.days // 365
print(f"Anda hidup: {umur_tahun} tahun, {umur_bulan} bulan")
