# data_str = "Tiswan ganteng abies"
# for huruf in data_str:
#     print(huruf)

batas = int(input("Masukan batas = "))
for i in range(1, batas + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(batas, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
