# -*- coding: utf-8 -*-
"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu dersimizde fonksiyonları gördük
Hata almamanız için programları ayrı ayrı çalıştırın
"""


def çıkar():
    sonuç = 74 - 15
    print(sonuç)

def topla():
    sonuç = 24 + 45
    print(sonuç)
#üstteki kodlarda fonksiyonu çağırmadığımız için çıktı almayız


def çıkar():
    sonuç = 74 - 15
    print(sonuç)

çıkar()

def topla():
    sonuç = 24 + 45
    print(sonuç)

topla()
#üstteki kodlarda fonksiyonu çağırdığımız için çıktı aldık


def çıkar(değer1,değer2):
    sonuç = değer1 - değer2
    print(sonuç)

çıkar(7,3)
çıkar(15,9)
çıkar(164,90)

def topla(değer1,değer2):
    sonuç = değer1 + değer2
    print(sonuç)

topla(7,3)
topla(15,9)
topla(164,90)
#üstteki kodlarda parametrize edip fonksiyonları kullandık


def çıkar(değer1,değer2):
    sonuç = değer1 - değer2
    return sonuç

çıkar(7,3)
çıkar(15,9)
çıkar(164,90)

def topla(değer1,değer2):
    sonuç = değer1 + değer2
    print(sonuç)

topla(7,3)
topla(15,9)
topla(164,90)
#üstteki kodlarda return ifadesini kullandığımız için ekrana çıktı vermedi


def çıkar(değer1,değer2):
    sonuç = değer1 - değer2
    return sonuç

print(çıkar(7,3))
print(çıkar(15,9))
print(çıkar(164,90))

def topla(değer1,değer2):
    sonuç = değer1 + değer2
    print(sonuç)

print(topla(7,3))
print(topla(15,9))
print(topla(164,90))
#üstteki kodlarda return ifadesini kullanıp döndürdükten sonra print kullandığımız için ekrana çıktı verdi
