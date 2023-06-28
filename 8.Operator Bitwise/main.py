a = 9
b = 5

# bitwise OR
c = a | b
print("======OR======")
print("nilai :", a, "binary : ", format(a, "08b"))
print("nilai :", b, "binary : ", format(b, "08b"))
print("---------------(OR)")
print("nilai :", c, "binary : ", format(c, "08b"))
print("---------------\n")


# bitwise AND
print("======AND======")
c = a & b
print("nilai :", a, "binary : ", format(a, "08b"))
print("nilai :", b, "binary : ", format(b, "08b"))
print("---------------(AND)")
print("nilai :", c, "binary : ", format(c, "08b"))
print("---------------")

# bitwise XOR
print("\n\n======XOR======")
c = a ^ b
print("nilai : ", a, "binary : ", format(a, "08b"))
print("nilai : ", b, "binary : ", format(b, "08b"))
print("---------------(XOR)")
print("nilai :", c, "binary : ", format(c, "08b"))
print("---------------")
