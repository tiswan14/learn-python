print ("====NOT====")
# Jadi datanya akan menjadi kebalikan
a = True
b = not a
print ('Data a : ', a)
print ('Data b : ', b)

#[OR]Jadi jika data salah satunya ada yang true maka hasilnya akan true 
print ("====OR====")
a = True
b = True
c = a or b
print (a, 'OR', b, '  =', c)

a = False
b = False
c = a or b
print (a, 'OR', b, '=', c)

a = True
b = False
c = a or b
print (a, 'OR', b, ' =', c)

a = False
b = True
c = a or b
print (a, 'OR', b, ' =', c)


#[AND]Akan true jika dua-duanya true
print ("====AND====")
a = True
b = True
c = a and b
print (a, 'AND', b, '  =', c)

a = False
b = False
c = a and b
print (a, 'AND', b, '=', c)

a = True
b = False
c = a and b 
print (a, 'AND', b, ' =', c)

a = False
b = True
c = a and b
print (a, 'AND', b, ' =', c)

#XOR | Akan true jika salah satunya ada true
print ("====XOR====")
a = True
b = True
c = a ^ b
print (a, 'XOR', b, '  =', c)

a = False
b = False
c = a ^ b
print (a, 'XOR', b, '=', c)

a = True
b = False
c = a ^ b 
print (a, 'XOR', b, ' =', c)

a = False
b = True
c = a ^ b
print (a, 'XOR', b, ' =', c)

