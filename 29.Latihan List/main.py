# Program List Daftar Buku
list_buku = []
while True:
    judul = input("Masukan Judul Buku   : ")
    penulis = input("Masukan Nama Penulis : ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    print(list_buku)

    print("\n\n", "=" * 10)
    for index, buku in enumerate(list_buku):
        print(f" {index+1} |  {buku[0]} |  {buku[1]} |")

    print("\n\n", "=" * 20)
    is_lanjut = input("Apakah akan lanjut? Y/N ")

    if is_lanjut == "n" or "N":
        break

print("Program kamu telah selesai sekian dan terimakasih")
