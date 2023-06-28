import os
import string


# Bentuk standard
def sepuluh_pangkat(argument: int) -> int:
    output = 10**argument
    return output


os.system("clear")
HASIL = sepuluh_pangkat(2)
print(HASIL)


def display(argument: string):
    print(argument)


display("maman")
