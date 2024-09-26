def diagram(width, ratio, even_sum, odd_sum):
    for lines in range(2):
        odd_pixels = round(width / (ratio + 1))
        even_pixels = width - odd_pixels
        print('\x1b[42m \x1b[0m' * even_pixels + '\x1b[45m \x1b[0m' * odd_pixels)
        print('Модуль суммы чисел' + ' ' * (width - 36) + 'Модуль суммы чисел')
        print('на чётных позициях' + ' ' * (width - 38) + 'на нечётных позициях')
        print(f'{even_sum} ({(ratio / (ratio + 1)):.1%})' + ' ' * (width - 26) + f'{odd_sum} ({(1 / (ratio + 1)):.1%})')

with open('sequence.txt') as file:
    numbers = list()
    for element in file:
        numbers.append(float(element))
    
    odd_sum = 0
    even_sum = 0
    for iterator in range(len(numbers)):
        if iterator % 2 == 0:
            even_sum += numbers[iterator]
        else:
            odd_sum += numbers[iterator]
    
    even_sum = round(abs(even_sum), 2)
    odd_sum = round(abs(odd_sum), 2)
    
    ratio = even_sum / odd_sum
    width = 50
    diagram(width, ratio, even_sum, odd_sum)