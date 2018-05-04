# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde format metodunu gördük
Hata almamanız için programları ayrı ayrı çalıştırın
"""

a = """
Türkçe: Günaydın
İngilizce: {} {}
"""

print(a)
#Bu şekilde bastırırsak normal çıktıyı elde ederiz


a = """
Türkçe: Günaydın
İngilizce: {} {}
""".format("Good","Morning")

print(a)
#Bu şekilde bastırırsak {} sembolun içine format metoduna yazdığımız değerleri sırasıyla yazabiliyoruz


a="python"

for i in a:
    print("bastırılan: {}".format(i))
#Bu şekilde de bastırabiliriz format metodu bu tarz programlarda daha çok işimize yarıyor


a = "|{:<15}|".format("Hakan")
print(a)
#Bu şekilde bastırdığımızda stringin sola yaslanmış olduğunu gördük


a = "|{:>15}|".format("Hakan")
print(a)
#Bu şekilde bastırdığımızda stringin sağa yaslanmış olduğunu gördük


a = "{} {}".format("Hakan","YILDIZ")
print(a)
#Hakan YILDIZ şeklinde bastırır


a = "{1} {0}".format("Hakan","YILDIZ")
print(a)
#YILDIZ Hakan şeklinde bastırır. 
#Hakan ı 0. indiste YILDIZ ı 1. indiste algılar 1 0 yazdığımız için ters bastırır


a = "{isim} {soyisim}".format(soyisim = "YILDIZ",isim = "Hakan")
print(a)
#İsim soyisim sırası doğru olduğu için Hakan YILDIZ bastırdı


a = "bu string {:s}".format(str(23))
# :s kodu string olduğunu belirtir burada hata almayız


a = "bu bir string {:s}".format(23) 
# string olduğu belirtilmediği için hata alırız


a = "bu bir sayı {:d}".format(23)
# :d kodu integer olduğunu belirtir burada hata almayız


a = "bu bir sayı {:d}".format(str(23))
#int olması gerekirken string belirtildiği için hata alırız


a = "{:,}".format(1234567890)
print(a)
#Sayıları basamaklarına ayırmaya yarar

