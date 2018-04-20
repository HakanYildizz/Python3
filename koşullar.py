"""
Hakan Yıldız
Bu dersimizde koşulları gördük
Hata almamanız için programları ayrı ayrı çalıştırın

öncelikle aşağıdakileri bilmemiz gerekiyor

==  eşittir

>=  büyük eşit

<=  küçük eşit

!=   <>  eşit değil
"""


#if örneği

#HATA : 5 ve 5ten küçük değer alınca herhangi brşey döndürmez

x = input("bir sayı giriniz:")
if int(x) > 5:
    print("x 5'ten büyük.")


#else örneği

#HATA : 5 değerini girersek 5ten küçük diye döndürür

x=input("bir sayı giriniz:")
if int(x) > 5:
    print("x 5'ten büyük.")
else:
    print("x 5'ten küçük.")
    
    
#elif örneği

#hatasız çalışır

x=input("bir sayı giriniz:")
if int(x) > 5:
    print("x 5'ten büyük.")
elif int(x) == 5:
    print("x 5'e eşit.")
else:
    print("x 5'ten küçük.")
    
