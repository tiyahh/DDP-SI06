import math

# BANGUN DATAR

def luas_persegi(sisi):
    luas = sisi * sisi
    print(f'Luas persegi, {sisi} * {sisi} = {luas}')

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print(f'Luas persegi panjang, {panjang} * {lebar} = {luas}')

def luas_segitiga(alas, tinggi):
    luas = 1/2 * alas * tinggi
    print(f'luas segitiga, 1/2 * {alas} * {tinggi} = {luas}')
    
def luas_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    print(f'Luas jajargenjang adalah, {alas} * {tinggi} = {luas}')

def luas_lingkaran(jari2):
    luas = 22/7 * jari2 * jari2
    print(f'Luas lingkaran adalah,22/7 * {jari2} * {jari2} = {luas}')

def layang2(d1, d2):
    luas = 1/2 * d1 * d2
    print(f'Luas layang-layang adalah, 1/2, {d1} * {d2} = {luas}')


# BANGUN RUANG

def luas_kubus(sisi):
    luas = 6 * sisi * sisi
    print(f'luas kubus adalah, 6 * {sisi} * {sisi} = {luas}')

def luas_balok(p,l,t):
    luas = 2 * (p*l + l*t + p*t)
    print(f'luas balok adalah, 2 * (({p}*{l}) + ({l}*{t}) + ({p}*{t})) = {luas}')

def luas_tabung(jari2, tinggi):
    luas = 2 * 22/7* jari2 * (jari2 + tinggi)
    print(f'luas tabung adalah, 2 * 22//7 * {jari2} * ({jari2} + {tinggi}) = {luas}')

def luas_kerucut(jari2, selimut):
    luas = 22/7 * jari2 * (jari2 + selimut)
    print(f'luas kerucut adalah, 22/7 * {jari2} * ({jari2} + {selimut}) = {luas}')

def luas_bola(jari2):
    luas = 4 * 22/7 * jari2 * jari2
    print(f'luas bola adalah, 4 * 22/7 * {jari2} * {jari2} = {luas}')


# PERHITUNGAN

import math

def tambah(bil1, bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)

def kurang(bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)

def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)

def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)