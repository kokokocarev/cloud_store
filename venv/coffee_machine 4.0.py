water_need = 200
milk_need = 50
beans_need = 15
one_cup = water_need + milk_need + beans_need
water_has = int(input())
milk_has = int(input())
cof_beans = int(input())
cups = int(input())
print("Write how many ml of water the coffee machine has:", water_has)
print("Write how many ml of milk the coffee machine has:", milk_has)
print("Write how many grams of coffee beans the coffee machine has:", cof_beans)
print("Write how many cups of coffee you will need:", cups)
if (water_has >= cups * water_need) and (milk_has >= cups * milk_need) and (cof_beans >= cups * beans_need):
    if (cups >= 0 and water_has > 0 and milk_has > 0 and cof_beans > 0):
        can_yes = min(water_has // water_need, milk_has // milk_need, cof_beans // beans_need)
        else_yes = can_yes - cups
        print("Yes, I can make that amount of coffee (and even", else_yes,"more than that)")
    else:
        print("Yes, I can make that amount of coffee")
