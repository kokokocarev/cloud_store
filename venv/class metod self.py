class PiggyBank:

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        if self.cents <= 99:
            self.dollars += deposit_dollars
            self.cents += deposit_cents
            if self.cents >= 100:
                 self.dollars += 1
                 self.cents -= 100
                 print(f'{self.dollars} dollar {self.cents} cents')
                 return self.dollars, self.cents
            print(f'{self.dollars} dollar {self.cents} cents')
            return self.dollars, self.cents
        else:
            print("Value of the attribute cents cannot be higher than 99!")
            return 0

bank = PiggyBank(int(input()), int(input()))
bank.add_money(int(input()), int(input()))