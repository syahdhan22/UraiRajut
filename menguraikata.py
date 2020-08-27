def urai(kata): 
    panjang =len(kata) #menghitung jumlah karakter
    hasil="" #membuat variable kosong
    for index in range(panjang+1): #menambahkan jumlah karakter setiap looping
        hasil+=kata[0:index] #hasil ditambah kata awal dan karakter yang ditambah setiap looping
    return hasil
print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))