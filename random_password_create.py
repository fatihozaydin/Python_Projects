import random
import string
import time

def generate_password(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))
    
while True:
    user_input = input("Enter a number to generate a random password or 'q' to quit: ")
    if user_input.isdigit():
        password = generate_password(int(user_input))
        print("Generated password:", password)
    elif user_input == 'q':
        print("Program Is Terminated...")
        time.sleep(1)
        break
        
    else:
        print("Please enter a number or 'q' to quit.")
