input_ = input('Enter cells: ')
input_ = [[input_[0], input_[1], input_[2]],
          [input_[3], input_[4], input_[5]],
          [input_[6], input_[7], input_[8]]]
numbers_s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
numbers_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def print_():
    print(f'''---------
| {input_[0][0]} {input_[0][1]} {input_[0][2]} |
| {input_[1][0]} {input_[1][1]} {input_[1][2]} |
| {input_[2][0]} {input_[2][1]} {input_[2][2]} |
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
        if input_[2][0] == '_':
            input_[2][0] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [1, 2]:
        if input_[1][0] == '_':
            input_[1][0] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [1, 3]:
        if input_[0][0] == '_':
            input_[0][0] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 1]:
        if input_[2][1] == '_':
            input_[2][1] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 2]:
        if input_[1][1] == '_':
            input_[1][1] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [2, 3]:
        if input_[0][1] == '_':
            input_[0][1] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 1]:
        if input_[2][2] == '_':
            input_[2][2] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 2]:
        if input_[1][2] == '_':
            input_[1][2] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()
    elif coord == [3, 3]:
        if input_[0][2] == '_':
            input_[0][2] = 'X'
            print_()
        else:
            print('This cell is occupied! Choose another one!')
            coord = input('Enter the coordinates: ').split()
            non_str()

print_()
coord = input('Enter the coordinates: ').split()
non_str()