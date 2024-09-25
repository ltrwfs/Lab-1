def grap(length):
    width = length//2
    for lines in range(length):
        position = lines//2
        print(' '*(width - position) + '\x1b[43m \x1b[0m' + ' '*position)

if __name__ == '__main__':
    length = 14
    grap(length)