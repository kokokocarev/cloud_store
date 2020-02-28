import random
database = 'banking.txt'
name_base = 'names.txt'
dict_ = dict()


def names():
    global list_names
    list_names = []
    file = open(name_base, 'r')
    read_ = file.readlines()
    for i in read_:
        list_names.append(i.replace('\n', ''))
    file.close()


def filling_file():
    global open_file
    open_file = open(database, 'w')
    for i in list_names:
        open_file.write(str(random.randint(0000000000000000, 9999999999999999)) + ' ' + i + ' '
                        + str(random.randint(0000, 9999)) + ' '
                        + str('%.2f' % random.uniform(1000.00, 100000.00)) + '\n')
    open_file.close()


def read_file():
    open_file = open(database, 'r')
    op_f = open_file.readlines()
    for i in op_f:
        i = i.split('\n')
        i = i[0]
        i = i.split()
        i[0] = int(i[0])
        i[1] = i[1] + ' ' + i[2]
        i[3] = int(i[3])
        i[4] = float(i[4])
        dict_[i[0]] = [i[1], i[3], i[4]]
    open_file.close()


def action_():
    global action, acc_num
    action = input('Please, choose the operation: balance - 1, transaction - 2, fill account - 3, exit - 4: ')
    if action == '4':
        print("Thank you for using our services!")
    while action != '4':
        if action == '1':
            for key, value in dict_.items():
                if acc_num == key:
                    print(f'Your balance: {value[2]}$')
            action_()
        elif action == '2':
            transaction()
        elif action == '3':
            fill()


def transaction():
    global action, transfer_account, transfer_amount, acc_num
    transfer_account = int(input('Please, enter account number for transfer: '))
    transfer_amount = int(input('Please, enter amount of money for transfer: '))
    for key, value in dict_.items():
        if transfer_account == key:
            value[2] += transfer_amount
        if acc_num == key:
            value[2] -= transfer_amount
    open_file = open(database, 'w')
    for key, value in dict_.items():
        open_file.write('{} {} {} {}\n'.format(key, value[0], value[1], value[2]))
    open_file.close()
    action_()


def fill():
    global action, transfer_account, transfer_amount, acc_num
    input_money = int(input('Please, enter cash amount: '))
    for key, value in dict_.items():
        if acc_num == key:
            value[2] += input_money
    open_file = open(database, 'w')
    for key, value in dict_.items():
        open_file.write('{} {} {} {}\n'.format(key, value[0], value[1], value[2]))
    open_file.close()
    action_()


def main():
    global acc_num
    read_file()
    acc_num = int(input('Enter your account number: '))
    pas = int(input('Enter your account password: '))
    for key, value in dict_.items():
        if acc_num == key and pas == value[1]:
            print(f'''Successful authorization for {value[0]}!
Welcome!''')
    action_()


main()
