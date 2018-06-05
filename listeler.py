# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde listeleri gördük
"""

ornek_liste = [1,"hakan",3.5]
print(ornek_liste)        #listeyi bastırdık
print(type(ornek_liste))  #listenin tipini bastırdık

liste1 = []
bos_liste = list()
#boş liste üstteki şekillerde olusşturulur

len(ornek_liste)
print(len(ornek_liste))
#burda 3 sonucunu göreceğiz 1. 1, 2. "hakan" , 3. de 3.5 değeridir

x = "Hakan"
liste2 = list(x)
print(liste2)
#herhangi bir karakteri listeye çevirebiliriz 

for i in dir(list()):
    if "__" not in i:
        print(i)
#burada işleyeceğimiz metotları listeledik

liste_kopya = ["hakan","yildiz"]
liste_kopya2 = liste_kopya[:]
print(liste_kopya)
print(liste_kopya2)
liste_kopya3 = ["hakan","yildiz"]
liste_kopya4 = list(liste_kopya3)
print(liste_kopya3)
print(liste_kopya4)
#listeleri kopyalayabiliriz

liste = ["a","b","c","d","e","f","g","h"]

liste[0]
print(liste[0])
#0. indeksteki elemanı bastırır

liste[3]
print(liste[3])
#3. indeksteki elemanı bastırır

liste[len(liste)-1]
print(liste[len(liste)-1])
#sonuncu indeksteki elemanı bastırır

liste[:4]
print(liste[:4])
#başlangıçtan 4. indekse kadar elemanları bastırır
#4. dahil değil

liste[1:5]
print(liste[1:5])
#1. indeksten 5. indekse kadar elemanları bastırır
#5. dahil değil


liste[3:]
print(liste[3:])
#3. indekseten sonuna kadar bastırır


liste[::2]
print(liste[::2])
#liste elemanlarını ikişer ikişer atlayarak bastırır

liste[::-1]
print(liste[::-1])
#listeyi tersten bastırır

liste3 =  [1,2,3,4,5]
liste4 =  [6,7,8,9,10]
print(liste3 + liste4)
#listeleri toplayabiliyoruz

liste5 = [1,2,3,4,5]
liste5 =  liste5 + ["Hakan"]
print(liste5)
#listeye eleman ekleyebiliyoruz

liste6 =[1,2,3,4,5]
liste6[4] = 10
liste6[:2] = [40,50]
print(liste6)
#listeleri indexini kullanarak değiştirebiliriz

liste7 = [10,20,30,40,50]
liste7 * 3
print(liste7)
#eşitleme yapmadığımız için liste değişmedi
liste7 = liste7 * 3 
print(liste7)
#listeleri tamsayılarla çarpabiliriz. eşitleme yaptığımız için değişti.

liste8 = [1,2,3,4,5,6,7]
liste8.append(34)
liste8.append("hakan")
print(liste8)
#append:listenin sonuna eleman eklemeyi sağlar

liste9 = [1,2,3,4,5,6,7,8,9,10]
liste9.clear()
print(liste9)
#clear:listenin içeriğini siler

liste10 = ["hakan","yildiz"]
liste11 = liste10.copy()
print(liste10)
print(liste11)
#copy:kopyalamamızı sağlar

liste12 = [1,2,3,4,5,1,2,2,3,2,2,3]
print(liste12.count(2))
print(liste12.count(3))
#count:bir elemanın listede kaç defa geçtiğini söyler

liste13 = [1,2,3,4,5,6,7]
liste13.extend([8,9,10])
print(liste13)
#extend:bir listeden başka bir listeye elemanlarını eklememizi sağlar

liste14 = [1,2,3,4,5,6,5,7,5,8,9,10]
print(liste14.index(5)) # 3 elemanı baştan başlayarak 4.indekste
print(liste14.index(5,7)) # 5 elemanı 7.indeksten itibaren arandığından 8.indekste
#index:verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler

liste15 = [1,2,3,4,5,6,7,8,9,10]
liste15.insert(3,"hakan") # 3.indekse "hakan" değerini ekliyoruz 
print(liste15)
#insert:listenin belli bir indeksine bir eleman eklememizi sağlar

liste16 = [1,2,3,4,5,6,7]
liste16.pop() # Son elemanı siler
liste16.pop(3) # 3.indeksteki elemanı siler
print(liste16)
#pop:içine hiçbir değer vermezsek listenin son elemanını silerek ekrana basar İçine belli bir indeks değeri verirsek o indeksi siler ve ekrana basar

liste17 = ["Python","Php","Java","C"]
liste17.remove("Python") 
liste17.remove("Java")
print(liste17)
#remove:verdiğimiz değeri listeden çıkarmamızı sağlar

liste18 = ["a", "b", "c","d","e"]
liste18.reverse()
print(liste18)
#reverse:listelerin ögelerini ters çevirmeye yarar

liste19 = [125,-12,33,1,134,10]
liste19.sort()
print(liste19)
liste20 = ["Python","Php","Ruby","C","Java"]
liste20.sort()
print(liste20)
#sort:bir listenin elemanlarını küçükten büyüğe sıralar

