class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance    
        #Private attribute var
    
    #Deposit methode: setter
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f"Deposited: {amount} tk. \nUpdated Balance: {self.__balance}")
    

    #Withdraw methode: getter
    def withdraw(self, amount):
        if(amount <= self.__balance):
            self.__balance = (self.__balance - amount)
            print(f"{amount} tk has been withdrawn. \nUpdated Balance: {self.__balance}")
        
        else:
            print ("You do not have sufficient balance in your account.")
            print ("Can't proceed. Transaction Canceled.")

    #Show the balance
    def get_balance(self):
        print(f"Current stored ammount: {self.__balance}")

#Account create user input
name = input("Enter the name of applicant:")
balance = float(input("Enter how much are you storing now:"))
acc = BankAccount(name, balance)

#Returning info and options
print ("Account Created.")
print("")

print(f"Account holder: {name} \nStored Ammount: {balance}")
print("")

print("Options for update:")
print("1. Deposit some money \n2. Withdraw some money \n3. Check the balance")

#option's act
while(True):
    print("")
    a = input("Enter the Serial No. of your requested process:")

    #Deposit
    if(a == "1"): 
        money = float(input("Enter how much are you depositing:"))
        acc.deposit(money)
    
    #Withdraw
    elif(a == "2"): 
        money = float(input("Enter how much do you want to withdraw:"))
        acc.withdraw(money)
    
    #Show balance
    elif(a == "3"):
        acc.get_balance()
    
    #Invalid
    else:
        print("Invalid request.")
