x = 10
y = 3
z = 5
#Tambah
hasil = x + y
print(x, '+' , y ,'=', hasil)

#Pengurangan
hasil = x - y
print(x, '-' , y ,'=', hasil)


#Perkalian
hasil = x * y
print(x, 'x' , y ,'=', hasil)


#Pembagian
hasil = int(x / y)
print(x, '/' , y ,'=', hasil)


#Eksponen/Perpangkatan
hasil = x ** y
print(x, '**' , y ,'=', hasil)

#Modulus
hasil = x % y
print(x, '%' , y ,'=', hasil)

#Floor Division #Kayak pembagian tapi dibulatkan kebawah
hasil = x // y
print(x, '//' , y ,'=', hasil)

#Prioritas Operasi
hasil = (x + y) * z
print('(',x, '+', y,')' ' *', z, '=', hasil) 

#Tanpa Prioritas
hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil) 
