# -*- coding: utf-8 -*-
"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu dersimizde hata bulmayı gördük
Kodları ayrı ayrı çalıştırmanızı öneririm
"""

try:
    a =  int("324234dsadsad") #ValueError
    print("hakan")
except: # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata")
print("bitti")

try:
 a = int(input("Sayı:"))
 b = int(input("Sayı:")) #ValueError 
 print(a / b)
except ValueError:
 print("değerleri doğru girin.")
except ZeroDivisionError:
 print("Bir sayı 0'a bölünemez.")

try:
    a = int(input("Sayı:"))
    b = int(input("Sayı:"))
    print(a / b) 
except (ValueError,ZeroDivisionError):
    print("ZeroDivision veya ValueError ")

try:
    a = int(input("Sayı:"))
    b = int(input("Sayı:"))
    print(a / b) #ZeroDivisionError
except ValueError:
    print("değerleri doğru girin")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez")
finally:
    print("Her zaman çalışırım")

# Verilen string'i ters çevirmek
def terscevir(a):
    if (type(a) != str):
        raise ValueError("Lütfen string ifade girin!")
    else:
        return a[::-1]
 print(terscevir("hakan"))
