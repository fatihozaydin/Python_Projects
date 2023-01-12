print("""********************
Kullanici Girişi:
********************
    """)

sys_kullanici_adi = ("fatih")
sys_parola = "123456"

kullanici_adi = input("Kullanici Adi: ")
parola = input("Parola: ")


if (sys_kullanici_adi == kullanici_adi and sys_parola != parola):
    print("Parola Hatali...")
elif (sys_kullanici_adi != kullanici_adi and sys_parola == parola):
    print("Kullanici Adi Hatali...")
elif (sys_kullanici_adi != kullanici_adi and sys_parola != parola):
    print("Kullanici Adi ve Parola Hatali...")
else:
    print("Sisteme Giriş Başariyla Yapildi...")
