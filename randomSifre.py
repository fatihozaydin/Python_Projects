import random
import string
import time

while True:
    
    def generate_password(length):
        password_chars = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        for i in range(length - 4):
            password += random.choice(password_chars)
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        return password

    password_length = int(input("Şifre uzunluğunu giriniz : "))
    print("Oluşturulan rastgele şifre : ",generate_password(password_length))
    time.sleep(0.5)