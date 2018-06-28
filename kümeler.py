# -*- coding: utf-8 -*-
"""
https://hakanyildiz23.wordpress.com/
Hakan Yıldız
Bu dersimizde kümeleri gördük
"""

küme = set()
print(type(küme))

küme1 = set([1,2,3,4,1])
print(type(küme1))
print(küme1)

küme2 = set((1,2,3,4))
print(type(küme2))
print(küme2)

küme3 = set("hakan")
print(type(küme3))
print(küme3)

for i in dir(set()):
    if "__" not in i:
        print(i)
#kümelerin metotları

küme4 = set(["muz", "kiraz", "vişne"])
küme4.add("çilek")
print(küme4)
#add:kümelere eleman eklemeye yarar

küme5 = set("hakan")
for i in küme5:
    print(i)
küme5.clear()
print(küme5)
#clear:kümenin içini boşaltmaya yarar

küme6 = set("istanbul")
küme6_yedek = küme6.copy()
print(küme6)
print(küme6_yedek)
#copy:bir kümeyi başka bir kümeye kopyalamamızı sağlar

küme7 = set([1, 2, 3, 5])
küme8 = set([3, 4, 2, 10])
print(küme7.difference(küme8)) #7de olup 8de olmayan
print(küme8.difference(küme7)) #8de olup 7de olmayan
#difference:iki kümenin farkını almamızı sağlar

küme9 = set([1, 2, 3])
küme10 = set([1, 3, 5])
küme9.difference_update(küme10) #küme9da olup küme10da olmayanı küme9a eşitle
print(küme9)
print(küme10)
küme9örn = set([1, 2, 3])
küme10örn = set([1, 3, 5])
küme10örn.difference_update(küme9örn) #küme10da olup küme9da olmayanı küme10a eşitle
print(küme9örn)
print(küme10örn)
#difference_update:difference() metodundan elde edilen sonuca göre kümenin güncellenmesini sağlar

küme11 = set(["istanbul", "izmir", "ağrı", "elazığ"])
küme11.discard("ağrı")
print(küme11)
küme11.discard("ankara")
#discard:kümeden öge silmemizi sağlar küme içinde bulunmayan ögeyi silmeye çalışırsak hata mesajı almayız

küme12 = set([1, 2, 3, 4])
küme13 = set([1, 3, 5, 7])
print(küme12.intersection(küme13))
küme12örn = set([1, 2, 3, 4]) 
küme13örn = set([1, 3, 5, 7]) 
print(küme12örn & küme13örn)
#intersection:kümelerin kesişim kümesini bulmamızı sağlar (&) işaretini kullanarak da kesişim kümesini bulabiliriz

küme14 = set([1, 2, 3])
küme15 = set([1, 3, 5])
küme14.intersection_update(küme15)
print(küme14)
print(küme15)
küme14örn = set([1, 2, 3]) 
küme15örn = set([1, 3, 5]) 
küme15örn.intersection_update(küme14örn) 
print(küme14örn) 
print(küme15örn)
#intersection_update:intersection() metodundan elde edilen sonuca göre kümenin güncellenmesini sağlar

küme16 = set([1, 2, 3])
küme17 = set([2, 4, 6])
print(küme16.isdisjoint(küme17))
küme16örn = set([1, 2, 3]) 
küme17örn = set([4, 5, 6]) 
print(küme16örn.isdisjoint(küme17örn))
#isdisjoint:kümelerin kesişim kümesinin boş olup olmadığını sorgulamamızı sağlar ortak eleman varsa False yoksa True döndürür

küme18 = set([1, 2, 3])
küme19 = set([0, 1, 2, 3, 4, 5])
print(küme18.issubset(küme19))
küme18örn = set([1, 2, 3, 9]) 
küme19örn = set([0, 1, 2, 3, 4, 5]) 
print(küme18örn.issubset(küme19örn))
#issubset:bir kümenin başka bir kümenin alt kümesi olup olmadığını sorgulamamızı sağlar

küme20 = set([1, 2, 3]) 
küme21 = set([0, 1, 2, 3, 4, 5]) 
print(küme21.issuperset(küme20))
küme20örn = set([1, 2, 3, 9]) 
küme21örn = set([0, 1, 2, 3, 4, 5]) 
print(küme21örn.issuperset(küme20örn))
#issuperset:bir kümenin başka bir kümeyi kapsayıp kapsamadığını sorgulamamızı sağlar

küme22 = set(["mersin", "trabzon", "edirne"])
print(küme22.pop()) # sildiğimiz elemanı gösterir
print(küme22)
#pop:kümelerin ögelerini rastgele silmemizi sağlar

küme23 = set(["istanbul", "izmir", "ağrı", "elazığ"]) 
küme23.remove("ağrı") 
print(küme23) 
küme23.remove("ankara") #hata
#remove:kümeden öge silmemizi sağlar küme içinde bulunmayan ögeyi silmeye çalışırsak hata mesajı alırız

a = set([1, 2, 5]) 
b = set([1, 4, 5])
print(a.symmetric_difference(b))
#symmetric_difference:iki kümede bulunmayan ögeleri aynı anda almamızı sağlar

küme26 = set([1, 2, 5]) 
küme27 = set([1, 4, 5])
küme26.symmetric_difference_update(küme27)
print(küme26)
print(küme27)
küme26örn = set([1, 2, 5]) 
küme27örn = set([1, 4, 5])
küme27örn.symmetric_difference_update(küme26örn)
print(küme26örn)
print(küme27örn)
#symmetric_difference_update:symmetric_difference() metodundan elde edilen sonuca göre kümenin güncellenmesini sağlar

küme28 = set([2, 4, 6, 8])
küme29 = set([1, 3, 5, 7])
print(küme28.union(küme29))
küme28örn = set([2, 4, 6, 8]) 
küme29örn = set([1, 3, 5, 7]) 
print(küme28örn | küme29örn)
#union:iki kümenin birleşimini almamızı sağlar (|) işaretini kullanarak da birleştirebiliriz

küme30 = set(["adana", "bodrum", "urfa"])
liste = [1, 2, 3]
küme30.update(liste)
print(küme30)
#update:bir kümeyi güncellememizi sağlar