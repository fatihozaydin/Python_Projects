import time

while True:
    for i in range(100):
        n_bottles = 99 - i
        print(f'{n_bottles} bottles of beer on the wall')
        print(f'{n_bottles} bottles of beer')
        if n_bottles > 0:
            print(f'take one down, pass it around')
            print(f'{n_bottles-1} bottles of beer on the wall')
        else:
            print('There are no more bottles of beer on the wall')
            print(f'99 bottles of beer on the wall')
        time.sleep(0.5)
    break
