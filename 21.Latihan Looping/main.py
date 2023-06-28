sisi = 10
count = 1
for i in range(sisi):
    print(" * " * count)
    count += 1

print()

count = 1
while True:
    if count % 2:
        print("*" * count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

count = 1
spasi = int(sisi / 2)
while True:
    if count % 2:
        print(" " * spasi, "+" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

sisi = 11
count = sisi
spasi = 0

while count >= 1:
    if count % 2:
        print(" " * spasi, "+" * count)
        spasi += 1
        count -= 1
    else:
        count -= 1
        continue

    if count < 1:
        break
