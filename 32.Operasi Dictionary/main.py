# Operator Dictionary
data_dict = {"cup": "Ucup surucup", "tong": "Otong surotong", "dung": "Dudung surudung"}

# Panjang Dictionary
len_dict = len(data_dict)
print(f"Panjang dictionary : {len_dict}")

# Mengecek key exist atau tidak
KEY = "tong"
checkey = KEY in data_dict
print(f"Apakah data '{KEY}' ada di dict : {checkey}")

# Mengakses value dengan menggunakan value(read) dengan get
print(data_dict["cup"])
# print(data_dict["kis"])Kalau tanpa get malah jadi error
print(data_dict.get("cup"))
print(data_dict.get("kis", "key tidak ditemukan"))  # Cek key dengan message

# Mengupdate data
data_dict["cup"] = "Ucup siganteng"
print(data_dict)
data_dict["sep"] = "Asep sikasep"
print(data_dict)

data_dict.update({"cup": "Ucup surucup"})
print(data_dict)

data_dict.update({"wan": "Tiswan sitampan"})
print(data_dict)

# Mendelete pada dictionary
del data_dict["wan"]
print(data_dict)
