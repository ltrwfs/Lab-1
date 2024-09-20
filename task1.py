def flag(length = 27, width = 6):
    
    for lines in range(width//3):
        line = ' '*length
        print(f'\x1b[41m{line}\x1b[0m')
    
    for lines in range(width//3):
        line = ' '*length
        print(f'\x1b[47m{line}\x1b[0m')
    
    for lines in range(width//3):
        line = ' '*length
        print(f'\x1b[44m{line}\x1b[0m')

if __name__ == '__main__':
    flag()