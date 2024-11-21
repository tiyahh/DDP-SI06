#1
print('\n---- celcius ke farenheit ----')

def celcius_ke_farenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_farenheit(14)

#2
print('\n---- Mencari bilangan genap----')

def is_genap(genap):
    print(genap %2 == 0)

is_genap(4)
is_genap(7)

#3
print('\n---- Keterangan lulus dan tidak lulus ----')

#rata2 nilai kelulusan 80
def skor(nilai):
    if nilai >= 70:
     print('lulus')
    else:
     print('Gagal')

skor(80)
skor(60)

#4
print('\n ---- Mencetak bilangan ganjil ----')

def bilangan_ganjil(ganjil):
    for i in range (1,ganjil+1, 2):
        print(i, end=' ')
bilangan_ganjil(20)

