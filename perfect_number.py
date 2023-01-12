
while True:

    number = input("Number:")
    if (number == "q"):
        print("Program Terminated...")
        break
    number = int(number)
    i = 1
    total = 0
    while (i < number):
        if (number % i == 0):
            total += i
        i += 1

    if (total == number):
        print(number,"This Number Is Perfect.")
    else:
        print(number,"This Number Isn't Perfect.")
