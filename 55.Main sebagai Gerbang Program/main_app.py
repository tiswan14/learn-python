# __main__ adalah sebagai gerbang program
# __name__ = __main__ akan terjadi jika kita run pada program pertama saja haha hehe
import fungsi


def tambah(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    angka1 = 10
    angka2 = 5
    hasil = tambah(angka1, angka2)
    print(f"hasil dari fugnsi = {hasil}")
