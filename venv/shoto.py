import numpy as np
input_ = input('Enter cells: ')
input_ = np.array([[input_[0], input_[1], input_[2]],
          [input_[3], input_[4], input_[5]],
          [input_[6], input_[7], input_[8]]])
count_x = np.count_nonzero(input_ == 'X')
count_o = np.count_nonzero(input_ == 'O')


def print_():
    print(f'''
               ---------
               | {input_[0][0]} {input_[0][1]} {input_[0][2]} |
               | {input_[1][0]} {input_[1][1]} {input_[1][2]} |
               | {input_[2][0]} {input_[2][1]} {input_[2][2]} |
               ---------''')


for i in input_:
    if all(['X', 'X', 'X'] == input_[0]) and all(['O', 'O', 'O'] == input_[1]):
        print_()
        print('Impossible')
        break
    if ['X', 'X', 'X'] in input_[0]\
    or ['X', 'X', 'X'] in input_[1]\
    or ['X', 'X', 'X'] in input_[2]\
    or ['X', 'X', 'X'] in input_[:, 0]\
    or ['X', 'X', 'X'] in input_[:, 1]\
    or ['X', 'X', 'X'] in input_[:, 2]\
    or input_[0][0] == 'X' and input_[1][1] == 'X' and input_[2][2] == 'X'\
    or input_[0][2] == 'X' and input_[1][1] == 'X' and input_[2][0] == 'X':
        print_()
        print('X wins')
        break
    if ['O', 'O', 'O'] in input_[0]\
    or ['O', 'O', 'O'] in input_[1]\
    or ['O', 'O', 'O'] in input_[2]\
    or ['O', 'O', 'O'] in input_[:, 0] \
    or ['O', 'O', 'O'] in input_[:, 1] \
    or ['O', 'O', 'O'] in input_[:, 2] \
    or input_[0][0] == 'O' and input_[1][1] == 'O' and input_[2][2] == 'O'\
    or input_[0][2] == 'O' and input_[1][1] == 'O' and input_[2][0] == 'O':
        print_()
        print('O wins')
        break