# with open("wanz.txt", "w", encoding="utf-8") as file:
#     file.write("Tiswan ")


with open(
    "wanz.txt", "w", encoding="utf-8"
) as file:  #'w' write dengan mengahapus semua file
    file.write("Hai sayang")

with open("wanz.txt", "a", encoding="utf-8") as file:  #'a' menambah data
    file.write("\nHai nona")
