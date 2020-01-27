class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        if self.c**2 == self.a**2+self.b**2:
            print('%.1f' % ((self.a * self.b)/2))
        else:
            print('Not right')


a = input()
#b = a.split()
#c = []
#for i in a.split():
#    i = [int(i)]
#    c.append(i[0])
#a_ = c[0]
#b_ = c[1]
#c_ = c[2]
#b = [int(i) for i in a.split()]
b = (list(map(int, a.split())))
a_ = b[0]
print(b)
b_ = b[1]
c_ = b[2]
test = RightTriangle(a_, b_, c_)
