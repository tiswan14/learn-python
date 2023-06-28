angka = 0
while angka < 10:
    angka += 1
    print(f"Angka sekarang -> {angka}")
    if angka == 3:
        print("Three")
        continue  # akan membuat loop loncat ke step selanjutnya
    elif angka == 4:
        print("Four")
        pass  # Tidak guna kecuali di function

    elif angka == 7:
        print("Berhenti paksa")
        break  #
    print("Good Game")
