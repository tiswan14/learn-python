import datetime

mahasiswa1 = {
    "nama": "Tiswan",
    "nim": "20305054",
    "sks_lulus": 144,
    "beasiswa": False,
    "tgl_lahir": datetime.datetime(2002, 8, 21),
}

mahasiswa2 = {
    "nama": "Asep Baskom",
    "nim": "20305055",
    "sks_lulus": 124,
    "beasiswa": False,
    "tgl_lahir": datetime.datetime(2003, 4, 13),
}

mahasiswa3 = {
    "nama": "Otong batong",
    "nim": "20305056",
    "sks_lulus": 112,
    "beasiswa": False,
    "tgl_lahir": datetime.datetime(2001, 1, 1),
}

data_mahasiswa = {
    "MAH01": mahasiswa1,
    "MAH02": mahasiswa2,
    "MAH03": mahasiswa3,
}

# print(data_mahasiswa)

print(f"{'KEY':<6} {'Nama':<14} {'SKS':<6} {'Beasiswa':<13} {'Lahir':<5}")
print("-" * 50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["tgl_lahir"].strftime("%x")
    print(f"{KEY:<6} {NAMA:<14} {SKS:<9} {BEASISWA:<10} {LAHIR}")
