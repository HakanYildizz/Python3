# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde kullanıcıdan veri almayı gördük
Hata almamanız için programları ayrı ayrı çalıştırın
"""

#input() fonksiyonu

ad = input("adınızı giriniz : ")
soyad = input("soyadınızı giriniz : ")

print("adınız",ad,"soyadınız",soyad,"dır.")


#burada hata almayız mesela 2 ile 3 girdik birleştirip sonuca 23 çıktısını verir
x = input("bir sayı giriniz : ")
y = input("bir sayı giriniz : ")

print(x+y)

#sonuç doğru
x = input("bir sayı giriniz : ")
y = input("bir sayı giriniz : ")

print(int(x)+int(y))

#üstteki örnekle aynı
x = int(input("bir sayı giriniz : "))
y = int(input("bir sayı giriniz : "))

print(x+y)


