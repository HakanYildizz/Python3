"""
https://hakanyildiz23.wordpress.com/
Hakan YILDIZ
Bu dersimizde veri yapılarını gördük
print i daha sonra anlatacagım yazdırma fonksiyonu şimdilik bunu bilseniz yeter
Bu dosyayı idle , pycharm veya sublime text yoluyla açabilirsiniz
Hata almamanız için programları ayrı ayrı çalıştırın
"""


print(type(5))                   #integer degerleri inceledik
print(type(49))

print(type(3.99))                #float değerleri inceledik
print(type(10.5))

print(type("hakanyildiz"))       #string değerleri inceleldik
print(type("123asd"))
print(type("100"))
print(type("87.3"))

print(type(bool(0)))                   #bool değerleri inceledik
print(type(bool("")))
print(type(bool('')))
print(type(bool("hakan")))
print(type(bool("python3")))
print(type(bool("40.5")))
print(type(bool('27')))

print(type(2.52))                #float değeri integer değere çevirme
print(type(int(2.52)))
print(type(15.99))
print(type(int(15.99)))

print(type(17))                  #integer değeri float değere çevirme
print(type(float(17)))
print(type(187))
print(type(float(187)))

print(type(20.76))               #integer,float değeri string değere çevirme
print(type(str(20.76)))
print(type(19))
print(type(str(19)))

print(type("3"))                #string değeri float,integer değere çevirme
print(type(float("3")))
print(type("28"))
print(type(int("28")))
print(type("47a"))              #hata alırız çünkü a string değer floata dönüşmez 
print(type(float("47a")))
print(type("59b"))              #hata alırız çünkü b string değer integera dönüşmez
print(type(int("59b")))
print(type("abcd"))             #hata alırız çünkü abcd string değer floata dönüşmez 
print(type(float("abcd")))
print(type("abcd"))             #hata alırız çünkü abcd string değer integera dönüşmez
print(type(int("abcd")))

print(bool(0))                  #string,integer,float değeri bool değere çevirme
print(bool(""))
print(bool(''))
print(bool(" "))                #bosluk bırakırsak true doner
print(bool(' '))                #bosluk bırakırsak true doner
print(bool('hakan'))
print(bool("python3"))
print(bool(40.5))
print(bool(27))
print(bool(234a))               #hata alırız 234a int deger degil str olması lazım onun için de " " yada ' ' içinde olmalı







