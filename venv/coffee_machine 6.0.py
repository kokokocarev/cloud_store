class CoffeeMachine:
    water = 400
    milk = 540
    cof_beans = 120
    dis_cups = 9
    money = 550

    def __init__(self, action):
        self.action = action

    def choosing_action(self):
        if self.action == "remaining":
            print()
            print("The coffee machine has:")
            print(CoffeeMachine.water, "of water")
            print(CoffeeMachine.milk, "of milk")
            print(CoffeeMachine.cof_beans, "of coffee beans")
            print(CoffeeMachine.dis_cups, "of disposable cups")
            print(CoffeeMachine.money, "of money")
            print()
        if self.action == "fill":
            global water_add, milk_add, cof_beans_add, dis_cups_add
            print()
            CoffeeMachine.water += int(input("Write how many ml of water do you want to add: "))
            CoffeeMachine.milk += int(input("Write how many ml of milk do you want to add: "))
            CoffeeMachine.cof_beans += int(input("Write how many grams of coffee beans do you want to add: "))
            CoffeeMachine.dis_cups += int(input("Write how many disposable cups of coffee do you want to add: "))
            print()
        if self.action == "take":
            print()
            print("I gave you", CoffeeMachine.money)
            CoffeeMachine.money -= CoffeeMachine.money
            print()
        if self.action == "buy":
            self.choosing_coffee()

    def choosing_coffee(self):
        self.money_buy = 0
        self.water_buy = 0
        self.milk_buy = 0
        self.cof_beans_buy = 0
        self.dis_cups_buy = 0
        print()
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if choice == '1':
            self.water_buy = 250
            self.cof_beans_buy = 16
            self.dis_cups_buy = 1
            self.money_buy = 4
            self.control_res()
        if choice == '2':
            self.water_buy = 350
            self.milk_buy = 75
            self.cof_beans_buy = 20
            self.dis_cups_buy = 1
            self.money_buy = 7
            self.control_res()
        if choice == '3':
            self.water_buy = 200
            self.milk_buy = 100
            self.cof_beans_buy = 12
            self.dis_cups_buy = 1
            self.money_buy = 6
            self.control_res()
        if choice == 'back':
            print()
            print("The coffee machine has:")
            print(CoffeeMachine.water, "of water")
            print(CoffeeMachine.milk, "of milk")
            print(CoffeeMachine.cof_beans, "of coffee beans")
            print(CoffeeMachine.dis_cups, "of disposable cups")
            print(CoffeeMachine.money, "of money")
            print()

    def control_res(self):
        if CoffeeMachine.water >= self.water_buy and CoffeeMachine.milk >= self.milk_buy and CoffeeMachine.cof_beans >= self.cof_beans_buy and CoffeeMachine.dis_cups >= self.dis_cups_buy:
            print("I have enough resources, making you a coffee!")
            CoffeeMachine.water -= self.water_buy
            CoffeeMachine.milk -= self.milk_buy
            CoffeeMachine.cof_beans -= self.cof_beans_buy
            CoffeeMachine.dis_cups -= self.dis_cups_buy
            CoffeeMachine.money += self.money_buy
        elif CoffeeMachine.water < self.water_buy:
            print("Sorry, not enough water!")
        elif CoffeeMachine.milk < self.milk_buy:
            print("Sorry, not enough milk!")
        elif CoffeeMachine.cof_beans < self.cof_beans_buy:
            print("Sorry, not enough coffee beans!")
        elif CoffeeMachine.dis_cups < self.dis_cups_buy:
            print("Sorry, not enough disposable cups!")
            print()


while __name__ == "__main__" :
    input_ = input("Write action (buy, fill, take, remaining, exit): ")
    coffee = CoffeeMachine(input_)
    if input_ == "exit":
        break
    else:
        coffee.choosing_action()
