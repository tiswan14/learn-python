#Membuat gabungan area rentang dari angka
# +++++3--------10+++++++
input_user = int(input('Masukan angka yang bernilai\nKurang dari 3\natau\nlebih dari 10 : '))

#Memeriksa angka kurang 3
is_kurang_dari = (input_user < 3)
print ('Kurang dari 3  = ', is_kurang_dari)

#Memeriksa angka lebih dari 10
is_lebih_dari = (input_user > 10)
print ('Lebih dari 10  =', is_lebih_dari)

is_correct =  is_kurang_dari or is_lebih_dari
print ('Anda yang anda masukan : ', is_correct)


#2
input_user = int(input('Masukan angka yang bernilai\nLebih dari 3\natau\nKurang dari 10 : '))
#Memeriksa angka lebih dari 3
is_kurang_dari = (input_user > 3)
print ('Kurang dari 3  = ', is_kurang_dari)

#Memeriksa angka kurang dari 10
is_lebih_dari = (input_user < 10)
print ('Lebih dari 10  =', is_lebih_dari)

is_correct =  is_kurang_dari or is_lebih_dari
print ('Anda yang anda masukan : ', is_correct)