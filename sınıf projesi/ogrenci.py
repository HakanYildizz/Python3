# -*- coding: utf-8 -*-
"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
"""

import _sqlite3

class Ogrenci():

    def __init__(self,numara,ad,soyad):

        self.numara = numara
        self.ad = ad
        self.soyad = soyad

    def __str__(self):

        return "Öğrenci Numarası: {}\nÖğrenci Adı: {}\nÖğrenci Soyadı: {}".format(self.numara,self.ad,self.soyad)

class Sinif():

    def __init__(self):
		
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = _sqlite3.connect("sinif.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists ogrenciler (numara INT,ad TEXT,soyad TEXT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()
		
    def baglantiyi_kes(self):
        
        self.baglanti.close()

    def ogrenci_ekle(self,ogrenci):

        sorgu = "Insert into ogrenciler Values(?,?,?)"

        self.cursor.execute(sorgu,(ogrenci.numara,ogrenci.ad,ogrenci.soyad))

        self.baglanti.commit()

    def ogrenci_sil(self,numara):

        sorgu = "Delete From ogrenciler where numara = ?"

        self.cursor.execute(sorgu,(numara,))

        self.baglanti.commit()
