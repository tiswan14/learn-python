# Copy Dictionary
teman_teman = {
    "cup": "Ucup surucup",
    "tong": "Otong surotong",
    "wan": "Tiswan sitampan",
}

friend = teman_teman
print(f"\nteman  : \n{teman_teman}")
print(f"friend : \n{friend}")

teman_teman["cup"] = "surubang"
print(f"\nteman  : \n{teman_teman}")
print(f"friend : \n{friend}")

friend = teman_teman.copy()
teman_teman["wan"] = "Tiswan    siganteng"
print(f"\nteman  : \n{teman_teman}")
print(f"friend : \n{friend}")

# Pop dictionary (Menstransfer key sesuai key yang ditentukan)
data_ucup = friend.pop("cup")  # Mentransfer data ke sini
print(f"\n\ndata ucup = {data_ucup}")
print(f"friend : \n{friend}")

# Pop item dictionary (Menstransfer key terakhir saja)
data_akhir = friend.popitem()
print(f"\n\ndata akhir = {data_akhir}")
print(f"friend : \n{friend}")
