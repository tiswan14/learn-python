import numpy as np

vektor_a = np.array([1, 2, 3, 4, 5])
list = [1, 2, 3, 4, 5]

print(f"List biasa = {list}")
print(f"Vektor a = {vektor_a}")
print(f"Vektor a kuadrat = {vektor_a**2}")
print(f"Vektor a x 5 = {vektor_a*5}")

matrik_b = np.array([(1, 2), (3, 4)])
print(f"matrik b = {matrik_b} ")
print(f"matrik b kuadrat = {matrik_b**2} ")

zeros_c = np.zeros((3, 3))
print(f"zeros c = \n{zeros_c}")

ones_c = np.ones((2, 2))
print(f"ones c = \n{ones_c}")

jumlah = matrik_b + matrik_b**2 + ones_c
print(f"Jumlah =\n {jumlah}")
