def graph(length):
    width = length//2
    print('↑')
    for lines in range(length):
        position = lines//2
        print('|'+' '*(width - position - 1) + '\x1b[43m \x1b[0m' + ' '*position)
    print('0' + '—'*width + '>')

if __name__ == '__main__':
    length = 14
    graph(length)