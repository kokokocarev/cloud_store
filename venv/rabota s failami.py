import random
dict_ = dict()
name_file = 'rps/rating.txt'
# content = [i.split() for i in open_file.read().split('\n')]
# content = '\n'.join(['{0}'.format(i) for i in open_file.read().split('\n')])

open_file = open(name_file, 'r')
op_f = open_file.readlines()
for i in op_f:
    i = i.split('\n')
    i = i[0]
    i = i.split()
    i[1] = int(i[1])
    dict_[i[0]] = i[1]
open_file.close()

name = input('Enter your name: ')
print('Hello,', name)


def zapis():
    for key, value in dict_.items():
        open_file.write('{} {}\n'.format(key, value))


def check():
    global name, input_, open_file
    input_ = input()
    if input_ == '!exit':
        print("Bye!")
    while input_ != '!exit':
        if input_ == '!rating' and name == 'Bob':
            print('Your rating:', dict_['Bob'])
            check()
        elif input_ == '!rating' and name == 'Jane':
            print('Your rating:', dict_['Jane'])
            check()
        elif input_ == '!rating' and name == 'Alex':
            print('Your rating:', dict_['Alex'])
            check()
        elif input_ == 'rock' or input_ == 'scissors' or input_ == 'paper':
            win()


def win():
    global input_, a, open_file
    a = random.choice(['scissors', 'paper', 'rock'])
    if input_ == a:
        print(f"There is a draw ({a})")
        if name == 'Bob':
            dict_['Bob'] += 50
        elif name == 'Jane':
            dict_['Jane'] += 50
        elif name == 'Alex':
            dict_['Alex'] += 50
    elif input_ == 'scissors' and a == 'rock':
        print(f"Sorry, but computer chose {a}")
    elif input_ == 'paper' and a == 'scissors':
        print(f"Sorry, but computer chose {a}")
    elif input_ == 'rock' and a == 'paper':
        print(f"Sorry, but computer chose {a}")
    elif a == 'scissors' and input_ == 'rock':
        print(f"Well done. Computer chose {a} and failed")
        if name == 'Bob':
            dict_['Bob'] += 100
        elif name == 'Jane':
            dict_['Jane'] += 100
        elif name == 'Alex':
            dict_['Alex'] += 100
    elif a == 'paper' and input_ == 'scissors':
        print(f"Well done. Computer chose {a} and failed")
        if name == 'Bob':
            dict_['Bob'] += 100
        elif name == 'Jane':
            dict_['Jane'] += 100
        elif name == 'Alex':
            dict_['Alex'] += 100
    elif a == 'rock' and input_ == 'paper':
        print(f"Well done. Computer chose {a} and failed")
        if name == 'Bob':
            dict_['Bob'] += 100
        elif name == 'Jane':
            dict_['Jane'] += 100
        elif name == 'Alex':
            dict_['Alex'] += 100
    open_file = open(name_file, 'w')
    zapis()
    open_file.close()
    check()


check()


