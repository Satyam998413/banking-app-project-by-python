# Banking app
# class based
# Withdraw and deposite
# write the transaction to a python file
# while True:
#     input()
#     classes65645455
#     meth_____open()==file operate
#     properties
class Bank:

    def __init__(self,initial_amount=0.00):#fdgbfxvdsfvgthfgdfgbt
        self.balance=initial_amount

    def log_transaction(self,transaction_string):#egtfgvdxgjgh
        with open("transaction.txt","a") as file:
            file.write(f"{transaction_string} \t\tBalace: {self.balance} \n\t")#dgthfgrdryhyfjhffhg

    def withdrwal(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
            self.balance=self.balance-amount
            self.log_transaction(f"Withdrew {amount}")

    def deposite(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        if amount:
            self.balance=self.balance+amount
            self.log_transaction(f"Deposited {amount}")

account=Bank(100)
while True:
    try:
        action=input("what kind of action do you want to take?")
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        break
    if action in ["withdrawal","deposite"]:
        if action is "withdrawal":
            amount=input("How much amount to take out ?")
            account.withdrawal(amount)
        else:
            amount=input("How much amount to put in ?")
            account.deposite(amount)

        print("Your Balance:\t",account.balance)
    else:
        print("That is not a valid action.Try again")

