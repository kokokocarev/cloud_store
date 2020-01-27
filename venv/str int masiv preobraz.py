input1 = [int(i) for i in input().split()]
input2 = int(input())
count = -1
result = []
for i in input1:
    count += 1
    if input2 == i:
        result.append(count)
        result = [str(i) for i in result]
if result == []:
    print('not found')
print(' '.join(result))

