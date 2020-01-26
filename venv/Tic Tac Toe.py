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
    if (input_[0][0] == '_')\
    or (count_x - count_o >= 2)\
    or (count_o - count_x >= 2)\
    or all(['X', 'X', 'X'] == input_[0]) and all(['O', 'O', 'O'] == input_[1])\
    or all(['X', 'X', 'X'] == input_[0]) and all(['O', 'O', 'O'] == input_[2])\
    or all(['X', 'X', 'X'] == input_[1]) and all(['O', 'O', 'O'] == input_[0])\
    or all(['X', 'X', 'X'] == input_[1]) and all(['O', 'O', 'O'] == input_[2])\
    or all(['X', 'X', 'X'] == input_[2]) and all(['O', 'O', 'O'] == input_[1])\
    or all(['X', 'X', 'X'] == input_[2]) and all(['O', 'O', 'O'] == input_[0]) \
    or all(['X', 'X', 'X'] == input_[:, 0]) and all(['O', 'O', 'O'] == input_[:, 1]) \
    or all(['X', 'X', 'X'] == input_[:, 0]) and all(['O', 'O', 'O'] == input_[:, 2]) \
    or all(['X', 'X', 'X'] == input_[:, 1]) and all(['O', 'O', 'O'] == input_[:, 0]) \
    or all(['X', 'X', 'X'] == input_[:, 1]) and all(['O', 'O', 'O'] == input_[:, 2]) \
    or all(['X', 'X', 'X'] == input_[:, 2]) and all(['O', 'O', 'O'] == input_[:, 1]) \
    or all(['X', 'X', 'X'] == input_[:, 2]) and all(['O', 'O', 'O'] == input_[:, 0]):
        print_()
        print('Impossible')
        break
    if all(['X', 'X', 'X'] == input_[0])\
    or all(['X', 'X', 'X'] == input_[1])\
    or all(['X', 'X', 'X'] == input_[2])\
    or all(['X', 'X', 'X'] == input_[:, 0])\
    or all(['X', 'X', 'X'] == input_[:, 1])\
    or all(['X', 'X', 'X'] == input_[:, 2])\
    or input_[0][0] == 'X' and input_[1][1] == 'X' and input_[2][2] == 'X'\
    or input_[0][2] == 'X' and input_[1][1] == 'X' and input_[2][0] == 'X':
        print_()
        print('X wins')
        break
    if all(['O', 'O', 'O'] == input_[0])\
    or all(['O', 'O', 'O'] == input_[1])\
    or all(['O', 'O', 'O'] == input_[2])\
    or all(['O', 'O', 'O'] == input_[:, 0])\
    or all(['O', 'O', 'O'] == input_[:, 1])\
    or all(['O', 'O', 'O'] == input_[:, 2])\
    or input_[0][0] == 'O' and input_[1][1] == 'O' and input_[2][2] == 'O'\
    or input_[0][2] == 'O' and input_[1][1] == 'O' and input_[2][0] == 'O':
        print_()
        print('O wins')
        break
    if (np.count_nonzero(input_[0] == '_') != 0\
    or np.count_nonzero(input_[1] == '_') != 0\
    or np.count_nonzero(input_[2] == '_') != 0)\
    and ():
        print_()
        print('Game not finished')
        break
    if np.count_nonzero(input_ == '_') == 0:
        print_()
        print('Draw')
        break
