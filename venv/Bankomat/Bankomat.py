# for names and filling_file
# import random
import time

database = 'banking.txt'
name_base = 'names.txt'
dict_ = dict()


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


class Bankomat:
    def __init__(self, action):
        self.action = action

    # Generate names for cards' owners
    # def names(self):
    #    self.list_names = []
    #    file = open(Bankomat.name_base, 'r')
    #    read_ = file.readlines()
    #    for i in read_:
    #        self.list_names.append(i.replace('\n', ''))
    #        file.close()

    # Fill file with card information
    # def filling_file(self):
    #    open_file = open(Bankomat.database, 'w')
    #    for i in self.list_names:
    #        open_file.write(str(random.randint(0000000000000000, 9999999999999999)) + ' ' + i + ' '
    #                       + str(random.randint(0000, 9999)) + ' '
    #                       + str('%.2f' % random.uniform(1000.00, 100000.00)) + '\n')
    #    open_file.close()

    def action_(self):
        if self.action == '5':
            print("Thank you for using our services!")
            exit()
        elif self.action == '1':
            for key, value in dict_.items():
                if acc_num == key:
                    print(f'Your balance: {value[2]}$')
        elif self.action == '2':
            self.transaction()
        elif self.action == '3':
            self.fill()
        elif self.action == '4':
            self.get()

    def transaction(self):
        self.transfer_account = int(input('Please, enter account number for transfer: '))
        self.transfer_amount = float(input('Please, enter amount of money for transfer: '))
        open_file = open(database, 'w')
        for key, value in dict_.items():
            if self.transfer_account == key:
                value[2] += self.transfer_amount
            if acc_num == key:
                value[2] -= self.transfer_amount
        for key, value in dict_.items():
            open_file.write('{} {} {} {}\n'.format(key, value[0], value[1], value[2]))
        open_file.close()

    def fill(self):
        self.input_money = float(input('Please, put cash in: '))
        print('Processing...')
        time.sleep(3)
        open_file = open(database, 'w')
        for key, value in dict_.items():
            if acc_num == key:
                value[2] += self.input_money
        for key, value in dict_.items():
            open_file.write('{} {} {} {}\n'.format(key, value[0], value[1], value[2]))
        open_file.close()

    def get(self):
        self.output_money = float(input('Please, enter cash amount to get: '))
        print('Counting the right amount...')
        time.sleep(3)
        print('Take it')
        open_file = open(database, 'w')
        for key, value in dict_.items():
            if acc_num == key:
                value[2] -= self.output_money
        for key, value in dict_.items():
            open_file.write('{} {} {} {}\n'.format(key, value[0], value[1], value[2]))
        open_file.close()


read_file()
acc_num = int(input('Enter your account number: '))
pas = int(input('Enter your account password: '))
for key, value in dict_.items():
    if acc_num == key and pas == value[1]:
        print(f'''Successful authorization for {value[0]}! 
Welcome!''')
        while __name__ == "__main__":
            bankomat = Bankomat(
                input('Please, choose the operation: balance - 1, transaction - 2, '
                      'fill account - 3, get money - 4, exit - 5: '))
            bankomat.action_()
    else:
         print('Wrong account number or password. Try again.')
         break