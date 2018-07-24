# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde ileri düzey fonksiyonları gördük
Detaylı öğrenmek için yukarıdaki linke gidebilirsiniz
"""

#lambda fonksiyonları

def fonksiyon(para1, para2):
    return para1 + para2
print(fonksiyon(3,5)
#def ile yapılışı

fonksiyon2 = lambda para1, para2: para1 + para2
print(fonksiyon2(2,4))
#lambda ile yapılışı

def çift_mi(sayı):
	return sayı % 2 == 0
print(çift_mi(14))
print(çift_mi(25)
#def ile yapılışı

çift_mi1 = lambda sayı: sayı % 2 == 0
print(çift_mi1(14))
print(çift_mi1(25))
#lambda ile yapılışı

for i in range(10):
	print(i**2)
#for ile yapılışı

print([i**2 for i in range(10)])
#lambda ile yapılışı


#özyinelemeli (recursive) fonksiyonlar


def faktöriyel(n):
	if n==1: 						#burada bitiş noktasını belirledik
		return 1
	else:                           #burada bitiş noktasına kadar olan döngüyü döndürdük
		return n*faktöriyel(n-1) 	
#Bu kodla faktöriyeli hesapladık
print("4!=", faktöriyel(4))
print("10!=", faktöriyel(10))
print("1!=", faktöriyel(1))


def fibonacci(n):
if n==1: #burada bitiş noktasını belirledik
return 1
elif n==2:
return 1
else: #burada bitiş noktasına kadar olan döngüyü döndürdük
return fibonacci(n-1)+fibonacci(n-2)
#Bu kodla fibonacciyi hesapladık
for i in range(1,20):
print(fibonacci(i), end="-")


def pascal(n):
if n == 1: #burada bitiş noktasını belirledik
return [1]
else: #burada bitiş noktasına kadar olan döngüyü döndürdük
x = [1]
y = pascal(n-1)
for i in range(len(y)-1):
x.append(y[i] + y[i+1])
x += [1]
return x
for i in range(1,11):
print(pascal(i))
#Bu kodla pascal üçgenini hesapladık