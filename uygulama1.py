"""
kullanıcı adı ve şifre kayıtlı olan bir programda kullanıcıdan veri almak
yapacağımız uygulamada daha iyi anlayacaksınız
"""
kullanici_adi = "hakanyildiz"
kullanici_sifre = "12345678"
#bu kısımda kullanıcı adımızı ve şifremizi belirttik

kullanici_isim = str(input("lütfen kullanıcı adınızı giriniz: "))
kullanici_parola = str(input("lütfen kullanıcı şifrenizi giriniz: "))
#burada kullanıcıdan adını ve şifresini istedik

if ((kullanici_adi == kullanici_isim) and (kullanici_sifre == kullanici_parola)):
    print("hoşgeldiniz!")
#bu kısımda kullanıcı adı ve parola eşleşirse "hoşgeldiniz!" bastırılır    

elif ((kullanici_adi != kullanici_isim) and (kullanici_sifre == kullanici_parola)):
    print("kullanıcı adınızı yanlış girdiniz, tekrar deneyiniz.")
#bu kısımda kullanıcı adı yanlış girilip kullanıcı şifresi doğru girilirse "kullanıcı adınızı yanlış girdiniz, tekrar deneyiniz." bastırılır

elif ((kullanici_adi == kullanici_isim) and (kullanici_sifre != kullanici_parola)):
    print("kullanıcı şifrenizi yanlış girdiniz, tekrar deneyiniz.")
#bu kısımda kullanıcı şifresi yanlış girilip kullanıcı adı doğru girilirse "kullanıcı şifrenizi yanlış girdiniz, tekrar deneyiniz." bastırılır

else:
    print("kullanıcı adınızı ve şifrenizi yanlış girdiniz, tekrar deneyiniz.")
#bu kısımda kullanıcı adı ve şifresi yanlış girilirse "kullanıcı adınızı ve şifrenizi yanlış girdiniz, tekrar deneyiniz." bastırılır    
#diğer konuları öğrendikçe örneklerimiz artacak kolay gelsin arkadaşlar    
