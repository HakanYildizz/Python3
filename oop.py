# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde nesne tabanlı programlamayı gördük
Hata almamanız için programları ayrı ayrı çalıştırın
"""
#sınıflar

class Notebook():
    marka =  "Lenovo"
    renk = "Siyah"

laptop1 = Notebook()  

#Notebook veri tipinde "laptop1" adında bir obje oluşturduk

print(laptop1.marka)

print(Notebook.renk)

#__init__() metodu

class Notebook():

    def __init__(self):
        print("init")

#self

class Notebook():

    def __init__(self,marka,renk):
        self.marka = marka
        self.renk = renk

laptop1 = Notebook("Lenovo","Siyah")

print(laptop1.marka)
print(laptop1.renk)

laptop2 = Notebook("HP","Kırmızı")

print(laptop2.marka)
print(laptop2.renk)

#varsayılan değer

class Notebook():

    def __init__(self,marka = "Belirtilmemiş",renk = "Belirtilmemiş"):
        self.marka = marka
        self.renk = renk

laptop1 = Notebook("HP")

print(laptop1.marka)
print(laptop1.renk)

#ayrı metod

class Notebook():

    def __init__(self,marka,renk,ram_boyutları):
        self.marka = marka
        self.renk = renk
        self.ram_boyutları = ram_boyutları

    def ürünbilgileri(self):
        print("""
Notebook Ürün Bilgisi
Marka : {}
Model : {}
Desteklenen Ram Boyutu : {}
        """.format(self.marka,self.renk,self.ram_boyutları))

    def ram_boyutu_ekle(self,yeni_ram_boyutu):
        self.ram_boyutları.append(yeni_ram_boyutu)

laptop1 = Notebook("Lenovo","Siyah",[4,8])

laptop1.ürünbilgileri()

laptop1.ram_boyutu_ekle(16)

laptop1.ürünbilgileri()

#kalıtım

class Öğrenci():

    def __init__(self,ad,soyad,yaş):
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş

    def bilgiler(self):
        print("öğrenci sınıfı")
        print("""
Ad : {}
Soyad : {}
Yaş : {}
        """.format(self.ad,self.soyad,self.yaş))

    def yaş_değiştir(self,yeni_yaş):
        print("Yaşı arttı.")
        self.yaş = yeni_yaş

class Öğretmen(Öğrenci):
    pass    #pass ile sonradan tanımlayabilirsin

öğretmen1 = Öğretmen("Hakan","Yıldız",19)

öğretmen1.bilgiler()

öğretmen1.yaş_değiştir(20)

öğretmen1.bilgiler()

#override

class Öğrenci():

    def __init__(self,ad,soyad,yaş):
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş

    def bilgiler(self):
        print("öğrenci sınıfı")
        print("""
Ad : {}
Soyad : {}
Yaş : {}
        """.format(self.ad,self.soyad,self.yaş))

    def yaş_değiştir(self,yeni_yaş):
        print("Yaşı arttı.")
        self.yaş = yeni_yaş

class Öğretmen(Öğrenci):

    def __init__(self,ad,soyad,yaş,öğrenci_sayısı):
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş
        self.öğrenci_sayısı = öğrenci_sayısı

    def bilgiler(self):
        print("öğretmen sınıfı")
        print("""
Ad : {}
Soyad : {}
Yaş : {}
Öğrenci Sayısı : {}
        """.format(self.ad,self.soyad,self.yaş,self.öğrenci_sayısı))

öğretmen1 = Öğretmen("Hakan","Yıldız",19,30)

öğretmen1.bilgiler()
#kalıtımın bir başka faydası da istersek öğrenci sınıfından yaş değiştirme metodunu kullanabiliyoruz
öğretmen1.yaş_değiştir(20)

öğretmen1.bilgiler()

#super

class Öğrenci():

    def __init__(self,ad,soyad,yaş):
        self.ad = ad
        self.soyad = soyad
        self.yaş = yaş

    def bilgiler(self):
        print("öğrenci sınıfı")
        print("""
Ad : {}
Soyad : {}
Yaş : {}
        """.format(self.ad,self.soyad,self.yaş))

    def yaş_değiştir(self,yeni_yaş):
        print("Yaşı arttı.")
        self.yaş = yeni_yaş

class Öğretmen(Öğrenci):

    def __init__(self,ad,soyad,yaş,öğrenci_sayısı):
        super().__init__(ad,soyad,yaş)
        self.öğrenci_sayısı = öğrenci_sayısı

    def bilgiler(self):
        print("öğretmen sınıfı")
        print("""
Ad : {}
Soyad : {}
Yaş : {}
Öğrenci Sayısı : {}
        """.format(self.ad,self.soyad,self.yaş,self.öğrenci_sayısı))

öğretmen1 = Öğretmen("Hakan","Yıldız",19,30)

öğretmen1.bilgiler()

öğretmen1.yaş_değiştir(20)

öğretmen1.bilgiler()
