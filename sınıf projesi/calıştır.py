# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
"""

from ogrenci import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Öğrenci Ekle

2. Öğrenci Sil 

Çıkmak için 'q' ya basın.
***********************************""")

sinif = Sinif()

while True:
    islem = input("Yapacağınız İşlem:")

    if (islem == "q"):
        
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break

    elif (islem == "1"):
        
        numara = input("Numara:")
        ad = input("Ad:")
        soyad = input("Soyad:")

        yeni_ogrenci = Ogrenci(numara,ad,soyad)

        print("Öğrenci ekleniyor....")

        sinif.ogrenci_ekle(yeni_ogrenci)
        print("Ogrenci Eklendi....")


    elif (islem == "2"):
        numara = input("Silmek istediğiniz öğrenci numarasını giriniz.")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E" or cevap == "e"):
            print("Öğrenci veritabanından siliniyor....")
            sinif.ogrenci_sil(numara)
            print("Öğrenci veritabanınıdan silindi....")

    else:
        print("Geçersiz işlem....")
