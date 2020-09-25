import time
from random import randint
from termcolor import colored

for i in range(1,45):
    print('')
play = 0
while play == 0:
    leftSpace = randint(8,80)
    loves = 8
    for i in range(1,17):
        count = leftSpace
        while count > 0:
            print(' ', end = '')
            count -= 1
        count = loves
        while count > 0:
            if i == 1 and count == 4:
                print('    ', end = '')
            elif i < 3 and count == 5:
                print('    ', end = '')
            else:
                print(colored('LOVE', 'red'), end = '')
            count -= 1
        if i < 5:
            leftSpace -= 2
            loves += 1
        else:
            leftSpace += 2
            loves -= 1
        time.sleep(0.3)
        print('\n', end ='')
    print('\n', end = '')
    time.sleep(0.3)
    count = randint(8,80)

    while count > 0:
        print(' ', end = '')
        count -= 1
    print(colored('H A P P Y B I R T H D A Y <3 <3 <3', 'magenta'))
    time.sleep(0.3)
    print('\n', end = '')
    time.sleep(0.3)