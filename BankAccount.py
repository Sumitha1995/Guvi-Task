# create Base Class BankAccount

class BankAccount:

    # constructor to initialize common attributes

    def __init__(self,account_number,balance):

        self.account_number=account_number
        self.__balance=balance      # encapsulation is done using private variable

    
    # deposit method

    def deposit(self,amount):

        self.__balance=self.__balance+amount
        print("Balance after deposit",self.__balance)

    
    # withdraw method

    def withdraw(self,amount):

        if amount<=self.__balance:

            self.__balance=self.__balance-amount
            print("Balance after withdrawal",self.__balance)

        else:

            print("Insufficient Balance")

    
    # getter method to access private variable

    def get_balance(self):

        return self.__balance


# Child class SavingsAccount inherited from Parent Class BankAccount

class SavingsAccount(BankAccount):

    # method to calculate interest

    def calculate_interest(self):

        interest=self.get_balance()*0.05
        print("Interest Amount is",interest)


# Child class CurrentAccount inherited from Parent Class BankAccount

class CurrentAccount(BankAccount):

    # overriding withdraw() method

    def withdraw(self,amount):

        minimum_balance=1000

        if self.get_balance()-amount>=minimum_balance:

            print("Withdrawal Successful")

        else:

            print("Minimum balance should be maintained")


# creating objects for child classes

s1=SavingsAccount(100,10000)
c1=CurrentAccount(102,5000)


# calling methods using objects

s1.deposit(2000)
s1.withdraw(1000)
s1.calculate_interest()

c1.withdraw(7500)