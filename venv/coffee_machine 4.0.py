water = 1200
milk = 540
cof_beans = 120
dis_cups = 9
money = 550
print("The coffee machine has:")
print(water ,"of water")
print(milk,"of milk")
print(cof_beans,"of coffee beans")
print(dis_cups,"of disposable cups")
print(money,"of money")

def take():
    global action
    action = input()
    money_out = money - money
    print("Write action (buy, fill, take):",action)
    print("I gave you $",money)
    print()
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(cof_beans, "of coffee beans")
    print(dis_cups, "of disposable cups")
    print(money_out, "of money")

def fill():
    global action
    action = input()
    print("Write action (buy, fill, take):", action)
    water_add = int(input())
    milk_add = int(input())
    cof_beans_add = int(input())
    dis_cups_add = int(input())
    print("Write how many ml of water do you want to add:", water_add)
    print("Write how many ml of milk do you want to add:", milk_add)
    print("Write how many grams of coffee beans do you want to add:", cof_beans_add)
    print("Write how many disposable cups of coffee do you want to add", dis_cups_add)
    print("The coffee machine has:")
    print(water + water_add, "of water")
    print(milk + milk_add, "of milk")
    print(cof_beans + cof_beans_add, "of coffee beans")
    print(dis_cups + dis_cups_add, "of disposable cups")
    print(money, "of money")

if action == "fill":
    fill()
if action == "take":
    take()

#def buy():
   # espresso =
   # latte =
   # cappuccino =
   # print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:", (int(input())))



