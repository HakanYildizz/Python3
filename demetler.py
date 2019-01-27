# -*- coding: utf-8 -*-
"""
https://hakannyildiz.wordpress.com/
Hakan Yıldız
Bu dersimizde demetleri gördük
"""

demet = (1,2,3,4,5,6,7,8,9,10)
print(demet)
print(type(demet))

demet1 = (1,)
print(demet1)
print(type(demet1))
#tek elemanlı demet bu şekilde tanımlanır

demet2 = (1,2,3,4,5,6,7)
print(demet2[0])
print(demet[4])
print(demet[2:])
#demetlerde de indekse ulaşabiliriz

for i in dir(tuple()):
	if "__" not in i:
		print(i)
#demetlerin metodları

demet3 = (1,23,36,34,28,1,42,5,1,1,34)
print(demet3.count(1)) 			#1den kaç tane olduğunu sorguladık
#count:bir değerin demette kaç defa geçtiğini söyler

demet4 = (152,422,381,"Hakan","Yıldız")
print(demet4.index("Hakan")) 	        #Hakan'ın kaçıncı indeksde olduğunu sorguladık
demet5 = (1,2,3,6,7,2,3,8)
print(demet5.index(2)) 			#2 değerinin baştan başlayarak kaçıncı indeksde olduğunu sorguladık
print(demet5.index(2,4))		#2 değerinin 4. indeksden başlayarak kaçıncı indeksde olduğunu sorguladık
#index:verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler
