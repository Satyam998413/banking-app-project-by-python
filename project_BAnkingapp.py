# Banking app
# class based
# Withdraw and deposite
# write the transaction to a python file
# while True:
#     input()
#     classes325343654
#     meth_____open()==file operate
#     properties
class Bank:
# sweghthgszfghju
    def __init__(self,initial_amount=0.00):
        self.balance=initial_amount

    def log_transaction(self,transaction_string):
        with open("transaction.txt","a") as file:
            file.write(f"{transaction_string} \t\tBalace: {self.balance} \n\t")

    def withdrwal(self,amount):
        try:
            amount=float(amount)
        except ValueError:
            amount=0
        # if amount:
        #     self.balance=self.balance-amount
        #     self.log_transaction(f"Withdrew {amount}")
# fdesdfhnjgfddgrthnm,jh
  
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
      

