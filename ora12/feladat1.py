class BankAccount:
    """Bankszámlák osztálya"""

    def __init__(self, name: str, account_number: str, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def egyenleg_kiiratas(self):
        print(self.balance)

    def befizetes(self, amount: int):
        self.balance += amount

    def withdrawal(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            print("Sikeres pénzfelvétel!")
        else:
            print("Sikertelen pénzfelvétel!")

    def __str__(self):
            return "Név: {}, bankszámlaszám: {}, egyenleg: {}".format(self.name, self.account_number, self.balance )


account1 = BankAccount("Béla", "00000000000", 100000)
account2 = BankAccount("János", "11111111111")
account1.egyenleg_kiiratas()
account2.egyenleg_kiiratas()
account1.withdrawal(50000)
account2.withdrawal(50000)
account1.egyenleg_kiiratas()
account2.egyenleg_kiiratas()
account1.befizetes(20000)
account2.befizetes(20000)
account1.egyenleg_kiiratas()
account2.egyenleg_kiiratas()

#beadando uj repositoryba, linket tanarnonek