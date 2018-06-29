# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde sözlükleri gördük
"""

sözlük = {}
sözlük1 = {"kitap": "book" , "kalem": "pencil"}
print(type(sözlük))
print(type(sözlük1))
print(len(sözlük))
print(len(sözlük1))

sözlük1örn = {"kitap": "book",
              "kalem": "pencil"}
print(type(sözlük1örn))
print(len(sözlük1örn))

print(sözlük1["kitap"])
print(sözlük1["kalem"])

sözlük2 = {"Hakan Yıldız": {"Memleket": "Elazığ",
                            "Meslek"  : "Öğrenci",
                            "Yaş"     : 19}}
print(sözlük2["Hakan Yıldız"]["Memleket"])
print(sözlük2["Hakan Yıldız"]["Meslek"])
print(sözlük2["Hakan Yıldız"]["Yaş"])

sözlük3 = {'a': '1', 
           'b': '2', 
           'c': '3'} 
print(sözlük3)
sözlük3['d'] = 4
print(sözlük3)

sözlük4 = {'a': '1', 
           'b': '2', 
           'c': '3',
           'd': '4'} 
print(sözlük4)
sözlük4['c'] = 9
print(sözlük4)

for i in dir(dict()):
    if "__" not in i:
        print(i)
#sözlüklerin metotları

sözlük5 = {'a': '1', 
           'b': '2', 
           'c': '3'} 
print(sözlük5)
sözlük5.clear()
print(sözlük5)
#clear:sözlüğün içini boşaltmaya yarar

sözlük6 = {'a': '1', 
           'b': '2', 
           'c': '3'} 
sözlük6örn = sözlük6.copy()
print(sözlük6)
print(sözlük6örn)
#copy:bir sözlüğü başka bir sözlüğe kopyalamamızı sağlar

harfler = 'a' , 'b' , 'c'
sözlük7 = dict.fromkeys(harfler, "harf")
print(sözlük7)
#fromkeys:anahtar(key) değerlerini otomatik olarak bir değere(value) eşitlememizi sağlar

sözlük8 = {"dil": "language", "bilgisayar": "computer", "masa": "table"}
sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız:")
print(sözlük8.get(sorgu, "Bu kelime veritabanımızda yoktur!"))
#get:parantez içine iki argüman alır birincisi anahtar değer ile sorgulamamızı sağlar ikincisi ise sorguya göre ne yazılacağını belirtir

sözlük9= {'a': 1, 'b': 2, 'c': 3} 
print(sözlük9.items())
#items:sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı sağlar

sözlük10 = {"a": 1,
            "b": 2,
            "c": 3,
            "d": 4}
print(sözlük10.keys())
#keys:anahtar sözcükleri öğrenmemizi sağlar

sözlük11 = {"a": 1, "b": 2, "c": 3, "d": 4} 
print(sözlük11)
sözlük11.pop("b")
print(sözlük11)
print(sözlük11.pop("z","öge yok"))
print(sözlük11.pop("f")) #hata
#pop:verilen argümanı silmemizi sağlar anahtar kelime eğer yoksa hata döndürür silinecek anahtarın yanına anlaşılır bir mesaj da yazabiliriz böylece anahtar kelime sözlükte bulunmuyorsa mesajı döndürür

sözlük12 = {"a": 1, "b": 2, "c": 3, "d": 4} 
print(sözlük12)
sözlük12.popitem()
print(sözlük12)
#popitem:son elemanı silmemizi sağlar

sözlük13 = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}
print(sözlük13)
sözlük13.setdefault("içecekler", ("su", "kola"))
print(sözlük13)
sözlük13.setdefault("meyveler", ("erik", "çilek"))
print(sözlük13)
#setdefault:sözlük içinde arama yapmamızı ve içinde eğer aradığımız anahtar değer çifti yoksa eklememizi sağlar

sözlük14 = {"a": 0, "b": 1, "c": 2, "d": 3} 
yenisözlük14 = {"a": 1, "b": 2, "c": 3, "d": 4} 
print(sözlük14)
print(yenisözlük14)
sözlük14.update(yenisözlük14)
print(sözlük14)
print(yenisözlük14)
#update:oluşturduğumuz sözlükleri yeni verilerle güncellememizi sağlar

sözlük15 = {"a": 1, "b": 2, "c": 3, "d": 4} 
print(sözlük15.values())
#values:değer sözcükleri öğrenmemizi sağlar
