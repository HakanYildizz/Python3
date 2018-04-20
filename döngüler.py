"""
Hakan Yıldız
Bu dersimizde döngüleri gördük
Hata almamanız için programları ayrı ayrı çalıştırın
"""


#for döngüsü

a = "hakanyildiz"
for harf in a:
    print(harf)
#bu programda a'nın içindeki harfleri satır satır bastırdık


#Alttaki üç program da aynı çıktıyı verir.
for i in range(0,10):
    print(int(i))    
#Bu programın 0'dan başladığını ve 9'da bittiğini görürüz. Belirtilmediği için 1'er 1'er artar. Bu program 10'u asla yazdırmaz.
    
for i in range(10):
    print(int(i))
#Kaçtan başlayacağını bilmediği için otomatik olarak 0'dan başlar. Belirtilmediği için 1'er 1'er artar. Bu program 10'u asla yazdırmaz.

for i in range(0,1,10):
    print(int(i))
#Bu programın 0'dan başladığını 1'er 1'er artarak 9'a kadar olacağını belirtir. Bu program 10'u asla yazdırmaz.  


#while döngüsü

x = 0
while x == 10:
    print ("hakan yıldız")
#bu program sonsuz döngüye girer

x = 0
while x <= 10:
    print ("hakan yıldız")
    x += 1
#Üstteki programda çıktı 11 kez yazdırır. Bunun sebebi ise program 10 kez döndükten sonra tekrar başa döner ve bir kez daha bastırır.

x = 0
while x <= 10:
    print (x)
    x += 1
#Çıktı bu sefer 10'a kadar bastırdı ancak 0'dan başladığı olduğu için yine 11 karakter bastırdı.    
