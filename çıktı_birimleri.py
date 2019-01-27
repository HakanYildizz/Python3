# -*- coding: utf-8 -*-
"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu dersimizde çıktı birimlerini gördük
Hata almamanız için programları ayrı ayrı çalıştırın
bu arada (#) ("""    """) bunları kullanarak yorum satırı ekleyebilirsiniz bu satır koda bir etki etmez
"""

#print fonksiyonu

print("hello world!")

#çıktılarında arada fark gözükmemesine rağmen ustteki in alttaki str. str ile işlem yapamazsınız.
print(3)
print("3")

print(type(3))
print(type("3"))

#sep parametresi

print("B","J","K")                #bunun çıktısı B J K olacaktır .Burada , olduğu için boşluk bırakıldı

print("B","J","K",sep = " ")      #bunun çıktısı B J K olacaktır . Burada ise sep parametresinin içinde boşluk var

print("B","J","K",sep = "")       #bunun çıktısı BJK olacaktır . Burada sep parametresinin içinde boşluk yok o yüzden BJK bitişik oldu

print("B","J","K",sep = ".")      #bunun çıktısı ise B.J.K olacaktır.

print("B","J","K",sep = "...")    #bunun çıktısı ise B...J...K olacaktır.

#end parametresi

print("B","J","K")                
print("Hakan","Yıldız")
"""
bunun çıktısı
B J K
Hakan Yıldız   
olur
"""

print("B","J","K",sep = "",end="")
print("Hakan","Yıldız")
"""
bunun çıktısı
BJKHakan Yıldız
olur BJK nin bitişik olmasının nedeni sep parametresinin içinde boşluk yok
"""

print("B","J","K",sep = ".",end="...")
print("Hakan","Yıldız")
"""
bunun çıktısı
B.J.K...Hakan Yıldız
olur B ile J nin sağındaki (.) sep parametresi yüzünden geldi K nın sağındaki (...) ise end parametresi yüzünden geldi 
"""

print("B","J","K",sep = "")
print("Hakan","Yıldız")
"""
bunun çıktısı
BJK
Hakan Yıldız
olur BJK nin bitişik olmasının nedeni sep parametresinin içinde boşluk yok
"""

print("B","J","K",sep = "",end = "\n")
print("Hakan","Yıldız")
"""
bunun çıktısı
BJK
Hakan Yıldız
olur 
BJK nin bitişik olmasının nedeni sep parametresinin içinde boşluk yok
end parametresi belirtilmediği taktirde \n kabul edilir yani o da alt satıra geçmemizi sağlar
"""
