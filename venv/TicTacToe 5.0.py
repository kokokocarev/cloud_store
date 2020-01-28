field = [[' ' for i in range(0, 3)],
          [' ' for i in range(3, 6)],
          [' ' for i in range(6, 9)]]
field = [[field[0][0], field[0][1], field[0][2]],
         [field[1][0], field[1][1], field[1][2]],
         [field[2][0], field[2][1], field[2][2]]]
numbers_s = [str(i) for i in range(0, 10)]
numbers_c = [int(i) for i in range(0, 10)]
col_1 = [col[0] for col in field]
col_2 = [col[1] for col in field]
col_3 = [col[2] for col in field]
count_x = field.count('X')
count_o = field.count('O')


def input_():
    global coord
    coord = input('Enter the coordinates: ').split()
    non_str()


def print_():
    print(f'''---------
| {field[0][0]} {field[0][1]} {field[0][2]} |
| {field[1][0]} {field[1][1]} {field[1][2]} |
| {field[2][0]} {field[2][1]} {field[2][2]} |
---------''')


def non_str():
    global coord
    for i in coord:
        if i not in numbers_s and i not in numbers_c:
            print('You should enter numbers!')
            coord = input('Enter the coordinates: ').split()
            non_str()
        else:
            coord = [int(i) for i in coord]
            if coord[0] > 3 or coord[1] > 3:
                print('Coordinates should be from 1 to 3!')
                coord = input('Enter the coordinates: ').split()
                non_str()
                break
            else:
                coord_()
                break


def coord_():
    global coord
    if coord == [1, 1]:
        if field[2][0] == ' ':
            field[2][0] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [1, 2]:
        if field[1][0] == ' ':
            field[1][0] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [1, 3]:
        if field[0][0] == ' ':
            field[0][0] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 1]:
        if field[2][1] == ' ':
            field[2][1] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 2]:
        if field[1][1] == ' ':
            field[1][1] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 3]:
        if field[0][1] == ' ':
            field[0][1] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 1]:
        if field[2][2] == ' ':
            field[2][2] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 2]:
        if field[1][2] == ' ':
            field[1][2] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 3]:
        if field[0][2] == ' ':
            field[0][2] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()


def stage_():
    for i in field:
        if (field[0][0] == '_') \
                or (count_x - count_o >= 2) \
                or (count_o - count_x >= 2) \
                or ['X', 'X', 'X'] == field[0] and ['O', 'O', 'O'] == field[1] \
                or ['X', 'X', 'X'] == field[0] and ['O', 'O', 'O'] == field[2] \
                or ['X', 'X', 'X'] == field[1] and ['O', 'O', 'O'] == field[0] \
                or ['X', 'X', 'X'] == field[1] and ['O', 'O', 'O'] == field[2] \
                or ['X', 'X', 'X'] == field[2] and ['O', 'O', 'O'] == field[0] \
                or ['X', 'X', 'X'] == field[2] and ['O', 'O', 'O'] == field[1] \
                or ['X', 'X', 'X'] == col_1 and ['O', 'O', 'O'] == col_2 \
                or ['X', 'X', 'X'] == col_1 and ['O', 'O', 'O'] == col_3 \
                or ['X', 'X', 'X'] == col_2 and ['O', 'O', 'O'] == col_1 \
                or ['X', 'X', 'X'] == col_2 and ['O', 'O', 'O'] == col_3 \
                or ['X', 'X', 'X'] == col_3 and ['O', 'O', 'O'] == col_1 \
                or ['X', 'X', 'X'] == col_3 and ['O', 'O', 'O'] == col_2:
            print_()
            print('Impossible')
            break
        if ['X', 'X', 'X'] == field[0] \
                or ['X', 'X', 'X'] == field[1] \
                or ['X', 'X', 'X'] == field[2] \
                or ['X', 'X', 'X'] == col_1 \
                or ['X', 'X', 'X'] == col_2 \
                or ['X', 'X', 'X'] == col_3 \
                or field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X' \
                or field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X':
            print_()
            print('X wins')
            break
        if ['O', 'O', 'O'] == field[0] \
                or ['O', 'O', 'O'] == field[1] \
                or ['O', 'O', 'O'] == field[2] \
                or ['O', 'O', 'O'] == col_1 \
                or ['O', 'O', 'O'] == col_2 \
                or ['O', 'O', 'O'] == col_3 \
                or field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O' \
                or field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O':
            print_()
            print('O wins')
            break
        if field.count('_') == 0:
            print_()
            print('Draw')
            break


def main():
    for i in field:
        print_()
        input_()
        break


main()