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

action = input()
print("Write action (buy, fill, take):",action)

def buy():
  choice = int(input())
  print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:",choice)
  if choice == 1:
      print("The coffee machine has:")
      print(water - 250, "of water")
      print(milk, "of milk")
      print(cof_beans - 16, "of coffee beans")
      print(dis_cups - 1, "of disposable cups")
      print(money + 4, "of money")
  elif choice == 2:
      print("The coffee machine has:")
      print(water - 350, "of water")
      print(milk - 75, "of milk")
      print(cof_beans - 20, "of coffee beans")
      print(dis_cups - 1, "of disposable cups")
      print(money + 7, "of money")
  elif choice == 3:
      print("The coffee machine has:")
      print(water - 200, "of water")
      print(milk - 100, "of milk")
      print(cof_beans - 12, "of coffee beans")
      print(dis_cups - 1, "of disposable cups")
      print(money + 6, "of money")
def take():
        money_out = money - money
        print("I gave you $",money)
        print()
        print("The coffee machine has:")
        print(water, "of water")
        print(milk, "of milk")
        print(cof_beans, "of coffee beans")
        print(dis_cups, "of disposable cups")
        print(money_out, "of money")

def fill():
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

if action == "take":
  take()
elif action == "fill":
  fill()
elif action == "buy":
  buy()