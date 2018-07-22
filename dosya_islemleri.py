# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde dosya işlemlerini gördük
Detaylı öğrnemek için yukarıdaki linke gidebilirsiniz
"""

#w dosya kipi

#aşağıdaki adda bir dosyanız varsa silinebilir dosya adını değiştirebilirsiniz

dosya = open("deneme1.txt","w",encoding="utf-8") #dosyayı bulunduğumuz dizinde açar
dosya.write("Hakan YILDIZ") #dosya içine yazı ekleme bu şekilde olur
dosya.close() #dosyayı kapatmamıza yarar

#dosya kapandıktan sonra aşağıdaki şekilde yazarsanız dosya silinip yeniden yazılır

dosya = open("deneme1.txt","w",encoding="utf-8")
dosya.write("Hakan")
dosya.close() 

#dosyayı bulunduğumuz dizinde açmak istemessek aşağıdaki şekilde yazmalıyız

dosya = open("C:/Users/user/Desktop/deneme1.txt","w",encoding="utf-8") # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
dosya.write("Hakan") 
dosya.close()

#a dosya kipi

dosya1 = open("deneme12.txt","a",encoding="utf-8") #dosyayı bulunduğumuz dizinde açar
dosya1.write("Hakan YILDIZ") #dosya içine yazı ekleme bu şekilde olur
dosya1.close() #dosyayı kapatmamıza yarar

#dosya kapandıktan sonra aşağıdaki şekilde yazarsanız dosyaya ekleme yapılır

dosya1 = open("deneme12.txt","a",encoding="utf-8")
dosya1.write("Hakan")
dosya1.close() 

#r dosya kipi

dosya2 = open("deneme123.txt","a",encoding="utf-8") #dosyayı bulunduğumuz dizinde açar
dosya2.write("Hakan YILDIZ\n") #dosya içine yazı ekleme bu şekilde olur
dosya2.write("Hakan\n")
dosya2.write("YILDIZ\n")
#başlangıçta dosya oluşturuyoruz

#for ile aşağıdaki şekilde dosya okunur 
dosya2 = open("deneme123.txt","r",encoding= "utf-8")# Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.
for i in dosya2: # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
	print(i) # Her bir satırı ekrana basıyoruz.
dosya2.close()

#read() fonksiyonu hiçbir değer vermessek bütün dosyayı okur
dosya2 = open("deneme123.txt","r",encoding="utf-8")
oku = dosya2.read()
print(oku)
dosya2.close()

#readline() fonksiyonu her çağrıldığında bir satır okur
dosya2 = open("deneme123.txt","r",encoding="utf-8")
print(dosya2.readline())
dosya2.close()

#readlines() dosyanın bütün satırlarını liste şeklinde döndürür
dosya2 = open("deneme123.txt","r",encoding="utf-8")
print(dosya2.readlines())
dosya2.close()

#x dosya kipi

dosya3 = open("deneme1234.txt","x",encoding="utf-8") #dosyayı bulunduğumuz dizinde açar
dosya3.write("Hakan YILDIZ") #dosya içine yazı ekleme bu şekilde olur
dosya3.close() #dosyayı kapatmamıza yarar

#dosya kapandıktan sonra aşağıdaki şekilde yazarsanız veya tekrar çalıştırırsanız hata alırsınız

dosya3 = open("deneme1234.txt","x",encoding="utf-8")
dosya3.write("Hakan")
dosya3.close() #hata

#r+ dosya kipi

dosya4 = open("deneme12345.txt","a",encoding="utf-8") #dosyayı bulunduğumuz dizinde açar
dosya4 = open("deneme12345.txt","r+",encoding="utf-8")
dosya4.write("python3\n")
dosya4.write("hakan\n")
dosya4.write("yıldız\n")
dosya4.write("Hakan Yıldız\n")
oku = dosya4.read()
print(oku)
dosya4.close()

#w+ dosya kipi

dosya5 = open("deneme123456.txt","w+",encoding="utf-8")
dosya5.write("python3\n")
dosya5.write("hakan\n")
dosya5.write("yıldız\n")
dosya5.write("Hakan Yıldız\n")
oku = dosya5.read()
print(oku)
dosya5.close()

#a+ dosya kipi

dosya6 = open("deneme1234567.txt","a+",encoding="utf-8")
dosya6.write("python3\n")
dosya6.write("hakan\n")
dosya6.write("yıldız\n")
dosya6.write("Hakan Yıldız\n")
oku = dosya6.read()
print(oku)
dosya6.close()

#dosya kapandıktan sonra aşağıdaki şekilde yazarsanız dosyaya ekleme yapılır

dosya6 = open("deneme1234567.txt","a+",encoding="utf-8")
dosya6.write("python3 dersleri\n")
oku = dosya6.read()
print(oku)
dosya6.close()

#x+ dosya kipi

dosya7 = open("deneme12345678.txt","x+",encoding="utf-8")
dosya7.write("python3\n")
dosya7.write("hakan\n")
dosya7.write("yıldız\n")
dosya7.write("Hakan Yıldız\n")
oku = dosya7.read()
print(oku)
dosya7.close()

#dosya kapandıktan sonra aşağıdaki şekilde yazarsanız veya tekrar çalıştırırsanız hata alırsınız

dosya7 = open("deneme12345678.txt","x",encoding="utf-8")
dosya7.write("Hakan")
dosya7.close() #hata


