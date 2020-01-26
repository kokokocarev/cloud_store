dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
input_ = input().split()
input1 = []

for i in input_:
    if i not in dictionary:
        input1.append(i)
if input1 == []:
    print("OK")
for i in input1:
    if input1 != []:
        print(i)