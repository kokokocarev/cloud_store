water = 400
milk = 540
cof_beans = 120
dis_cups = 9
money = 550

action = input(("Write action (buy, fill, take, remaining, exit): "))

def remaining():
    print()
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(cof_beans, "of coffee beans")
    print(dis_cups, "of disposable cups")
    print(money, "of money")
    print()

def take():
    print()
    print("I gave you", money)
    print()

def buy():
    global money_buy, water_buy, milk_buy, cof_beans_buy, dis_cups_buy
    money_buy = 0
    water_buy = 0
    milk_buy = 0
    cof_beans_buy = 0
    dis_cups_buy = 0
    print()
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    if choice == '1':
        water_buy = 250
        cof_beans_buy = 16
        dis_cups_buy = 1
        money_buy = 4
    if choice == '2':
        water_buy = 350
        milk_buy = 75
        cof_beans_buy = 20
        dis_cups_buy = 1
        money_buy = 7
    if choice == '3':
        water_buy = 200
        milk_buy = 100
        cof_beans_buy = 12
        dis_cups_buy = 1
        money_buy = 6
    if choice == 'back':
        remaining()


def fill():
    global water_add, milk_add, cof_beans_add, dis_cups_add
    print()
    water_add = int(input("Write how many ml of water do you want to add: "))
    milk_add = int(input("Write how many ml of milk do you want to add: "))
    cof_beans_add = int(input("Write how many grams of coffee beans do you want to add: "))
    dis_cups_add = int(input("Write how many disposable cups of coffee do you want to add: "))
    print()

while action:
    if action == 'buy':
        buy()
        if water >= water_buy and milk >= milk_buy and cof_beans >= cof_beans_buy and dis_cups >= dis_cups_buy:
            print("I have enough resources, making you a coffee!")
            water -= water_buy
            milk -= milk_buy
            cof_beans -= cof_beans_buy
            dis_cups -= dis_cups_buy
            money += money_buy
        elif water < water_buy:
            print("Sorry, not enough water!")
        elif milk < milk_buy:
            print("Sorry, not enough milk!")
        elif cof_beans < cof_beans_buy:
            print("Sorry, not enough coffee beans!")
        elif dis_cups < dis_cups_buy:
            print("Sorry, not enough disposable cups!")
        print()
        action = input(("Write action (buy, fill, take, remaining, exit): "))
    if action == 'fill':
        fill()
        water += water_add
        milk += milk_add
        cof_beans += cof_beans_add
        dis_cups += dis_cups_add
        action = input(("Write action (buy, fill, take, remaining, exit): "))
    if action == 'take':
        take()
        money -= money
        action = input(("Write action (buy, fill, take, remaining, exit): "))
    if action == 'remaining':
        remaining()
        action = input(("Write action (buy, fill, take, remaining, exit): "))
    if action == 'exit':
        break