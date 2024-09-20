def pattern(width):
    pixel = '\x1b[43m  \x1b[0m'
    print((pixel + '  '*3) * 2 * width + pixel)
    print(('  ' + pixel) * 4 * width + '  ')
    print(('  '*2 + pixel + '  '*3 + pixel + '  ') * width + '  ')
    print(('  ' + pixel) * 4 * width + '  ')
    print((pixel + '  '*3) * 2 * width + pixel)

if __name__ == '__main__':
    width = 10
    length = 5
    for lines in range(length):
        pattern(width)
        print('\x1b[2A')