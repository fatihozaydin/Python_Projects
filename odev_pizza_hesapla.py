

def get_input(text):

    user_input = input(text + ': ')

    if user_input.isdigit():

        return int(user_input)
    else: 

        print('Lütfen bir sayı giriniz!!!!')

        return get_input(text)


def create_pizza(size):

    diameter = get_input(f'{size} pizza için çap')

    price = get_input(f'{size} pizza için fiyat')

    return {

        'diameter': diameter,
        'price': price,
    }


def get_pizza_area(diameter):
    r = diameter / 2
    area = 3.14 * (r ** 2)
    return area


def calculate_score(pizza):

    area = get_pizza_area(pizza['diameter'])
    score = area / pizza['price']

    return score


def main():

    small_pizza = create_pizza('Küçük')
    large_pizza = create_pizza('Büyük')

    small_score = calculate_score(small_pizza)
    large_score = calculate_score(large_pizza)

    print(
        '\nVerimlilikler:\n    Küçük: {}\n    Büyük: {}\n'.format(
            round(small_score, 2), round(large_score, 2)
        )
    )

    if small_score > large_score:
        print('Küçük pizza daha verimlidir!')

    elif large_score > small_score:
        print('Büyük pizza daha verimlidir!')

    else:
        print('Pizzacınız takıntılı bir matematik mühendisidir!')


main()
