#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Depositedâ‚¹{}. New balance: {}".format(amount,self.__account_balance))
        else:
            print("Invalid deposit amount please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdraw â‚¹{}. New balance: {}".format(amount,self.__account_balance))
        else:
            print("Invalid withdrawal amount pr insufficient balance.")

    def display_balance(self):

      print("Account balance for{}(Account #{}:â‚¹{}.".format(self.__account_holder_name,self.__account_number,self.__account_balance))
        

# create an instance of the Bank Account class 

account=BankAccount(account_number="1234567890",account_holder_name="jhon",initial_balance=5000.0)

#Test deposit and withdrawal Functionally.

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Depositedâ‚¹{}. New balance: {}".format(amount,self.__account_balance))
        else:
            print("Invalid deposit amount please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdraw â‚¹{}. New balance: {}".format(amount,self.__account_balance))
        else:
            print("Invalid withdrawal amount pr insufficient balance.")

    def display_balance(self):

      print("Account balance for{}(Account #{}:â‚¹{}.".format(self.__account_holder_name,self.__account_number,self.__account_balance))
        

# create an instance of the Bank Account class 

account=BankAccount(account_number="1234567890",account_holder_name="jhon",initial_balance=5000.0)

#Test deposit and withdrawal Functionally.

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
