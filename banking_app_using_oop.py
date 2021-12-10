#Banking System using OOP

#Parent Class : User
#Holds details about an user
#Has a function to show user details

#Child Class : Bank
#Stores details about the account balance
#Stores details about the account
#Allows for deposits, withdraw, view_balance

#Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Personal Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient funds | Balance Available : $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Your current account balance is : $", self.balance)














            
