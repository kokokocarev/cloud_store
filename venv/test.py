count = int(input())
number = 0
inputs = []
while count != 0:
    number += count
    inputs.append(count * count)
    if number == 0:
        a = sum(inputs)
        print(a)
        break
    else:
        count = int(input())
