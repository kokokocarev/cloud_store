field = [[' ' for i in range(0, 3)],
         [' ' for i in range(3, 6)],
         [' ' for i in range(6, 9)]]
field = [[field[0][0], field[0][1], field[0][2]],
         [field[1][0], field[1][1], field[1][2]],
         [field[2][0], field[2][1], field[2][2]]]
numbers_s = [str(i) for i in range(0, 10)]
counter = 0


def input_():
    global coord
    while stage_() is not None:
        print(stage_())
        break
    else:
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
    if coord[0] not in numbers_s or coord[1] not in numbers_s:
        print('You should enter numbers!')
        coord = input('Enter the coordinates: ').split()
        non_str()
    else:
        coord = [int(i) for i in coord]
        if coord[0] > 3 or coord[1] > 3:
            print('Coordinates should be from 1 to 3!')
            coord = input('Enter the coordinates: ').split()
            non_str()
        else:
            coord_()


def coord_():
    global coord, counter
    if coord == [1, 1]:
        if field[2][0] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[2][0] = 'O'
            else:
                field[2][0] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [1, 2]:
        if field[1][0] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[1][0] = 'O'
            else:
                field[1][0] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [1, 3]:
        if field[0][0] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[0][0] = 'O'
            else:
                field[0][0] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 1]:
        if field[2][1] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[2][1] = 'O'
            else:
                field[2][1] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 2]:
        if field[1][1] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[1][1] = 'O'
            else:
                field[1][1] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 3]:
        if field[0][1] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[0][1] = 'O'
            else:
                field[0][1] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 1]:
        if field[2][2] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[2][2] = 'O'
            else:
                field[2][2] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 2]:
        if field[1][2] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[1][2] = 'O'
            else:
                field[1][2] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 3]:
        if field[0][2] == ' ':
            counter += 1
            if counter % 2 == 0:
                field[0][2] = 'O'
            else:
                field[0][2] = 'X'
            print_()
            stage_()
            input_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()


def stage_():
    global coord, col_1, col_2, col_3, count_x, count_o
    col_1 = [col[0] for col in field]
    col_2 = [col[1] for col in field]
    col_3 = [col[2] for col in field]
    count_x = field[0].count('X') + field[1].count('X') + field[2].count('X')
    count_o = field[0].count('O') + field[1].count('O') + field[2].count('O')
    if ['X', 'X', 'X'] == field[0] \
            or ['X', 'X', 'X'] == field[1] \
            or ['X', 'X', 'X'] == field[2] \
            or ['X', 'X', 'X'] == col_1 \
            or ['X', 'X', 'X'] == col_2 \
            or ['X', 'X', 'X'] == col_3 \
            or (field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X')\
            or (field[0][2] == 'X' and field[1][1] == 'X' and field[2][0] == 'X'):
        return 'X wins'
    elif ['O', 'O', 'O'] == field[0] \
            or ['O', 'O', 'O'] == field[1] \
            or ['O', 'O', 'O'] == field[2] \
            or ['O', 'O', 'O'] == col_1 \
            or ['O', 'O', 'O'] == col_2 \
            or ['O', 'O', 'O'] == col_3 \
            or (field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O') \
            or (field[0][2] == 'O' and field[1][1] == 'O' and field[2][0] == 'O'):
        return 'O wins'
    elif (field[0].count(' ') == 0
            and field[1].count(' ') == 0
            and field[2].count(' ') == 0):
        return 'Draw'


def main():
    print_()
    input_()


main()
