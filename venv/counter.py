from collections import Counter
scores = input().split()
count = 0
taunt = 0
for i in scores:
    if i == 'I':
        count += 1
        if count == 3:
          print('Game over')
          print(taunt)
          break
    if i == 'C':
        taunt += 1
if count != 3:
    c = Counter(scores)
    c = c['C']
    print('You won')
    print(c)