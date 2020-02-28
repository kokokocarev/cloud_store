input_ = input('Enter cells: ')
input_ = [[input_[0], input_[1], input_[2]],
          [input_[3], input_[4], input_[5]],
          [input_[6], input_[7], input_[8]]]
col_1 = [col[0] for col in input_]
col_2 = [col[1] for col in input_]
col_3 = [col[2] for col in input_]
count_x = input_.count('X')
count_o = input_.count('O')


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
    or ['X', 'X', 'X'] == input_[0] and ['O', 'O', 'O'] == input_[1]\
    or ['X', 'X', 'X'] == input_[0] and ['O', 'O', 'O'] == input_[2]\
    or ['X', 'X', 'X'] == input_[1] and ['O', 'O', 'O'] == input_[0]\
    or ['X', 'X', 'X'] == input_[1] and ['O', 'O', 'O'] == input_[2]\
    or ['X', 'X', 'X'] == input_[2] and ['O', 'O', 'O'] == input_[0]\
    or ['X', 'X', 'X'] == input_[2] and ['O', 'O', 'O'] == input_[1]\
    or ['X', 'X', 'X'] == col_1 and ['O', 'O', 'O'] == col_2\
    or ['X', 'X', 'X'] == col_1 and ['O', 'O', 'O'] == col_3\
    or ['X', 'X', 'X'] == col_2 and ['O', 'O', 'O'] == col_1\
    or ['X', 'X', 'X'] == col_2 and ['O', 'O', 'O'] == col_3\
    or ['X', 'X', 'X'] == col_3 and ['O', 'O', 'O'] == col_1\
    or ['X', 'X', 'X'] == col_3 and ['O', 'O', 'O'] == col_2:
        print_()
        print('Impossible')
        break
    if ['X', 'X', 'X'] == input_[0]\
    or ['X', 'X', 'X'] == input_[1]\
    or ['X', 'X', 'X'] == input_[2]\
    or ['X', 'X', 'X'] == col_1\
    or ['X', 'X', 'X'] == col_2\
    or ['X', 'X', 'X'] == col_3\
    or input_[0][0] == 'X' and input_[1][1] == 'X' and input_[2][2] == 'X'\
    or input_[0][2] == 'X' and input_[1][1] == 'X' and input_[2][0] == 'X':
        print_()
        print('X wins')
        break
    if ['O', 'O', 'O'] == input_[0]\
    or ['O', 'O', 'O'] == input_[1]\
    or ['O', 'O', 'O'] == input_[2]\
    or ['O', 'O', 'O'] == col_1\
    or ['O', 'O', 'O'] == col_2\
    or ['O', 'O', 'O'] == col_3\
    or input_[0][0] == 'O' and input_[1][1] == 'O' and input_[2][2] == 'O'\
    or input_[0][2] == 'O' and input_[1][1] == 'O' and input_[2][0] == 'O':
        print_()
        print('O wins')
        break
    if (input_[0].count('_') != 0
    or input_[1].count('_') != 0
    or input_[2].count('_') != 0):
        print_()
        print('Game not finished')
        break
    if input_.count('_') == 0:
        print_()
        print('Draw')
        break
