
while True:

    sayı = input("Sayı:")
    if (sayı == "q"):
        print("Program Sonlandırıldı...")
        break
    sayı = int(sayı)
    i = 1
    toplam = 0
    while (i < sayı):
        if (sayı % i == 0):
            toplam += i
        i += 1

    if (toplam == sayı):
        print(sayı,"mükemmel bir sayıdır.")
    else:
        print(sayı,"mükemmel bir sayı değildir.")
