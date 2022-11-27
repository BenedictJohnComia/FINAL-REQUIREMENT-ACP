from BankSystem import bankSystem
from MainMenuMethods import MainMenuYesOrNo

class atmSystem(bankSystem):
    def __init__(self, customerID):
        self.customerJsonToDict()
        self.bankMonetaryJsonToDict()
        self.customerID = customerID
        self.customerBalance = self.customerDatabase[str(self.customerID)]["Balance:"]
        self.customerLoan = self.customerDatabase[str(self.customerID)]["Loan:"]
        self.customerPin = self.customerDatabase[str(self.customerID)]["Pin:"]
        self.customerPinCount = 3
        
    def addMoney(self):
        try:
            self.customerJsonToDict()
            self.bankMonetaryJsonToDict()
            
            print("\nDEPOSIT MONEY")
            print("How much money do you want to deposit?")
            depositMoney = float(input("Enter amount: "))
            while True:
                print(f"\nAre you sure you want to deposit ₱{depositMoney}? ")
                MainMenuYesOrNo()
                choiceDeposit = int(input("Enter choice: "))
                if choiceDeposit == 1:
                    while True:
                        customerInputPin = int(input("Enter your pin: "))
                        if customerInputPin == self.customerPin:
                            self.customerDatabase[str(self.customerID)]["Balance:"] = self.customerBalance + depositMoney
                            self.bankMonetaryCollection["Bank Balance:"] = float(self.bankMonetaryCollection["Bank Balance:"] + depositMoney)
                            self.addToCustomerJsonFile()
                            self.addToBankMonetaryJsonFile()
                            print("Deposit Successful!")
                            return
                        else:
                            pinCount = self.pinCount()
                            if pinCount == False: return
                                                                                   
                elif choiceDeposit == 2:
                    return
                else:
                    print("\nInvalid Input. Please try again")
        
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
        
    def removeMoney(self):
        try:
            self.customerJsonToDict()
            self.bankMonetaryJsonToDict()
            
            print("\nWITHDRAW MONEY")
            print("How much money do you want to withdraw?")
            withdrawMoney = float(input("Enter amount: "))
            if withdrawMoney > self.customerBalance:
                print(f"\nYou are withdrawing an amount that exceeds your balance which is {self.customerBalance}")
                return
            
            while True:
                print(f"\nAre you sure you want to withdraw ₱{withdrawMoney}? ")
                MainMenuYesOrNo()
                choiceDeposit = int(input("Enter choice: "))
                if choiceDeposit == 1:
                    while True:
                        customerInputPin = int(input("Enter your pin: "))
                        if customerInputPin == self.customerPin:
                            self.customerDatabase[str(self.customerID)]["Balance:"] = self.customerBalance - withdrawMoney
                            self.bankMonetaryCollection["Bank Balance:"] = float(self.bankMonetaryCollection["Bank Balance:"] - withdrawMoney)
                            self.addToCustomerJsonFile()
                            self.addToBankMonetaryJsonFile()
                            print("Withdraw Successful!")
                            return
                        else:
                            pinCount = self.pinCount()
                            if pinCount == False: return
                                                                                
                elif choiceDeposit == 2:
                    return
                else:
                    print("\nInvalid Input. Please try again")
        
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
        
    def payLoan(self):
        try:
            self.customerJsonToDict()
            self.bankMonetaryJsonToDict()
            
            print("\nPAY LOAN")
            if self.customerLoan == 0:
                print("You have no loan to pay.")
                return
           
            print("How much loan do you want to pay?")
            payLoanMoney = float(input("Enter amount: "))
            if  payLoanMoney > self.customerLoan:
                print(f"\nYou are paying an amount that exceeds your loan which is {self.customerLoan}")
                return
            
            while True:
                print(f"\nAre you sure you want to pay a loan of ₱{payLoanMoney}? ")
                MainMenuYesOrNo()
                choiceDeposit = int(input("Enter choice: "))
                if choiceDeposit == 1:
                    while True:
                        customerInputPin = int(input("Enter your pin: "))
                        if customerInputPin == self.customerPin:
                            self.customerDatabase[str(self.customerID)]["Loan:"] = self.customerLoan - payLoanMoney
                            self.bankMonetaryCollection["Bank Balance:"] = float(self.bankMonetaryCollection["Bank Balance:"] + payLoanMoney)
                            self.addToCustomerJsonFile()
                            self.addToBankMonetaryJsonFile()
                            print("Loan Payment Successful!")
                            return
                        else:
                            pinCount = self.pinCount()
                            if pinCount == False: return
                                                                                
                elif choiceDeposit == 2:
                    return
                else:
                    print("\nInvalid Input. Please try again")
    
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
         
    def checkBalance(self):
        print("\nCHECK BALANCE")
        print(f"Your current balance is {self.customerBalance}")

    def pinCount(self):
        self.customerPinCount = self.customerPinCount - 1
        if self.customerPinCount == 0:
            print("\nYou reached the max amount of tries. Please try again.")
            self.customerPinCount = 3
            return False
        else: 
            print(f"\nIncorrect Pin. Please try again. You have {self.customerPinCount} tries left")