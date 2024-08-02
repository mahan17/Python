class BankAccount:
    defaultAccNumber = 1

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

        else:
            print("Deposit Amount must be Greater than Zero")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Not enough balance!")
                print("Total Balance : ",self.balance)
        else:
            print("Enter amount greater than '0'")
    
    def get_balance(self):
        return f'Current Balance is {self.balance}'
    
acc1 = BankAccount("Mahan",10000)
acc1.deposit(20000)
print(f'Mahan"s {acc1.get_balance()}')                                                     # Output = Mahan"s Current Balance is 30000
acc1.withdraw(2000)
print(f'{acc1.name} account Number is {acc1.defaultAccNumber} and {acc1.get_balance()}')   # Output = Mahan account Number is 2 and Current Balance is 28000

acc2 = BankAccount("Gopal",10000)
acc2.deposit(10000)
print(f'{acc2.name} account number is {acc2.defaultAccNumber} and {acc2.get_balance()}')   # Output = Gopal account number is 3 and Current Balance is 20000
