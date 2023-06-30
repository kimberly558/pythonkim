class Bankaccount:
    def __init__(self, accno, hname, bal=0):
        self.accountnumber = accno
        self.holdername = hname
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient funds")

    def display_balance(self):
        print(f"accountnumber: {self.accountnumber}")
        print(f"holdername: {self.holdername}")
        print(f"balance: {self.balance}")


myaccount = Bankaccount(549, "Kim", 6000)
myaccount.display_balance()
myaccount.deposit(1000)
myaccount.display_balance()
myaccount.withdraw(60000)
myaccount.display_balance()
