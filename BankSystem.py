from MainMenuMethods import MainMenuVerifyInfo, MainMenuCustomerDatabase
from CustomerInformationInquiry import customerInfo
import collections
import json

class bankSystem:
    def __init__(self):
        self.customerDatabase = collections.defaultdict(dict)
        self.bankMonetaryCollection = {}
        self.customerJsonToDict()
        self.bankMonetaryJsonToDict()
        self.customerID = int(self.customerNewID()) 
        self.accountNumber = int(self.customerNewAccNum())
        self.bankBalance = self.bankMonetaryCollection["Bank Balance:"]
        self.mintTotal = self.bankMonetaryCollection["Mint Total:"]
        self.burnTotal = self.bankMonetaryCollection["Burn Total:"]
        self.initialDepositTotal = self.bankMonetaryCollection["Initial Deposit Total:"]
        self.activityLog = []
        self.mintCount = 5
     
    def mintMoney(self):
        try:
            print("\nMINT MONEY")
            print("The minting limit is currently at Php 50,000.00")
            print(f"You have {self.mintCount} mints left.")
            if self.mintCount <= 5 and self.mintCount >= 1:
                addMoney = float(input("Enter amount to be minted: "))
                if addMoney < 0 or addMoney > 50000.00:
                    print("\nInvalid Input. Please try again.")
                    return
                
                self.mintCount = self.mintCount - 1
                self.mintTotal = self.mintTotal + addMoney
                self.bankBalance = self.bankBalance + addMoney
                self.bankMonetaryCollection["Mint Total:"] = self.mintTotal
                self.bankMonetaryCollection["Bank Balance:"] = self.bankBalance
                
                print(f"The mint total is {self.mintTotal}") 
                print(f"The current balance of bank is {self.bankBalance}") 
                
                self.addToBankMonetaryJsonFile()
            else:
                print("\nYou reached the max limit for minting money today.")
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not a number. Please try again.")
        
    def burnMoney(self):
        try:
            print("\nBURN MONEY")
            if self.bankBalance == 0.0:
                print("\nThere are no funds to be burned.")
            else:
                burnMoney = float(input("Enter amount to be burned: "))
                if burnMoney < 0 or burnMoney > self.bankBalance:
                    print("\nInvalid Input. Please try again")
                    return
                
                self.burnTotal = self.burnTotal + burnMoney
                self.bankBalance = self.bankBalance - burnMoney
                self.bankMonetaryCollection["Burn Total:"] = self.burnTotal
                self.bankMonetaryCollection["Bank Balance:"] = self.bankBalance
                
                print(f"The burn total is {self.burnTotal}") 
                print(f"The current balance is {self.bankBalance}") 
                
                self.addToBankMonetaryJsonFile()
                
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not a number. Please try again.")
        
    def openAccount(self):
        try:
            print("\nOPEN ACCOUNT")
            print(f"Enter information for customer {self.customerID}")
            customerObj = customerInfo()
            customerObj.accountNumber = self.accountNumber
            customerObj.customerID = self.customerID
            customerObj.balance = self.initialDepositAcc()
                
            while True:
                customerObj.displayInfo()
                print("[1] Yes, That is correct")
                print("[2] No, I want to change some information")
                choiceVerify = int(input("Enter your choice: "))
                if choiceVerify == 2:
                    MainMenuVerifyInfo()
                    while True:
                        choiceChange = int(input("Enter your choice: "))
                        if choiceChange == 1:
                            customerObj.firstName = str(input("Enter first name: "))
                            break
                        elif choiceChange == 2:
                            customerObj.lastName = str(input("Enter last name: "))
                            break
                        elif choiceChange == 3:
                            customerObj. age = int(input("Enter age: "))
                            break
                        elif choiceChange == 4:
                            customerObj.address = str(input("Enter address: "))
                            break
                        elif choiceChange == 5:
                            customerObj.pin = int(input("Enter pin: "))
                            break
                        elif choiceChange == 6:
                            customerObj.username = input("Enter username: ")
                            break
                        elif choiceChange == 7:
                            customerObj.password = input("Enter password: ")
                            break
                        elif choiceChange == 8:
                            customerObj.balance = self.initialDepositAcc()
                            break
                        elif choiceChange == 9:
                            break
                        else:
                            print("Invalid Input. Please try again.")
                            
                elif choiceVerify == 1:
                    self.customerDatabase[self.customerID] = {}
                    self.customerDatabase[self.customerID]["First Name:"] =  customerObj.firstName
                    self.customerDatabase[self.customerID]["Last Name:"] = customerObj.lastName
                    self.customerDatabase[self.customerID]["Age:"] = customerObj.age
                    self.customerDatabase[self.customerID]["Address:"] = customerObj.address
                    self.customerDatabase[self.customerID]["Account Number:"] = customerObj.accountNumber
                    self.customerDatabase[self.customerID]["Pin:"] = customerObj.pin
                    self.customerDatabase[self.customerID]["Username:"] = customerObj.username
                    self.customerDatabase[self.customerID]["Password:"] = customerObj.password
                    self.customerDatabase[self.customerID]["Balance:"] = customerObj.balance
                    self.customerDatabase[self.customerID]["Credit Level:"] = customerObj.creditLevelofCustomer
                    self.customerDatabase[self.customerID]["Loan Limit:"] = customerObj.loanLimitAcc
                    self.customerDatabase[self.customerID]["Loan:"] = customerObj.loan
                    break
                else:
                    print("Invalid Input. Please try again.")
  
            self.initialDepositTotal = self.initialDepositTotal + customerObj.balance
            self.bankBalance = self.bankBalance + customerObj.balance
            self.bankMonetaryCollection["Initial Deposit Total:"] = self.initialDepositTotal
            self.bankMonetaryCollection["Bank Balance:"] = self.bankBalance
            print(f"The initial deposit total is {self.initialDepositTotal}") 
            print(f"The current balance of bank is {self.bankBalance}") 
            self.customerID = self.customerID + 1
            self.accountNumber = self.accountNumber + 1
            self.addToCustomerJsonFile()
            self.addToBankMonetaryJsonFile()
            
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not an integer. Please try again.")
        
        except TypeError as e:
            print("\nThe", e)
            print ("An invalid input caused this error")
            
        except AttributeError as e:
            print("\nThe program", e)
            print ("An invalid input caused this error")
            
    def loanAssesment(self):
        try:
            self.customerJsonToDict()
            
            print("\nLOAN ASSESSMENT")
            choiceCustomer = int(input("Enter ID of customer: "))
            customerExistence = self.checkCustomerExistence(choiceCustomer)
            if customerExistence == False: return
            
            choiceCustomer = str(choiceCustomer)
            customerCreditLevel = int(self.customerDatabase[choiceCustomer]["Credit Level:"])
            customerLoan =  float(self.customerDatabase[choiceCustomer]["Loan:"])
            customerLoanLimit = float(self.customerDatabase[choiceCustomer]["Loan Limit:"])
            customerLoanInterestRate = self.customerLoanInterestRate(customerCreditLevel)
            print(f"Customer {choiceCustomer} currently has a loan amounting to {customerLoan}.")
            print(f"The loan limit of Customer {choiceCustomer} is {customerLoanLimit}.")
            
            if customerCreditLevel == 1:
                print(f"Customer {customerCreditLevel} cannot loan in the bank because he/she has no tier.")
                return
            else:
                print(f"Bank Balance: {self.bankBalance}")
                loanAmount = float(input("How much money will be loaned: "))
                if loanAmount > self.bankBalance:
                    print(f"\nYou entered an amount that exceeds the bank balance.")
                elif loanAmount > customerLoanLimit:
                    print(f"\nYou entered an amount that exceeds the loan limit of Customer {choiceCustomer}")
                elif loanAmount <= 0:
                    print(f"\nYou entered an invalid amount")
                else:
                    currentLoan = self.customerDatabase[choiceCustomer]["Loan:"]
                    loanWithInterest = (loanAmount + (customerLoanInterestRate * loanAmount)) + currentLoan
                    if loanWithInterest > customerLoanLimit:
                        print(f"\nThe current loan exceeds the loan limit which is {customerLoanLimit}")
                        print("Sorry for the inconvenience. Please try again.")
                    else:
                        print("\nThe following transactions are made: ")
                        print(f"Loan placed: {loanAmount}")
                        print(f"Loan to be payed (with annual interest): {loanWithInterest}")
                        
                        self.customerDatabase[choiceCustomer]["Loan:"] = float(loanWithInterest)
                        self.addToCustomerJsonFile()
          
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not a number. Please try again.") 
                 
    def accessCustomerDatabase(self):
        try:
            while True:
                MainMenuCustomerDatabase()
                choiceCustomerDatabase = int(input("Enter your choice: "))
                if choiceCustomerDatabase == 1:
                    self.showCustomerDatabase()
                elif choiceCustomerDatabase == 2:
                    choiceCustomer = int(input("Enter ID of customer to be searched: "))
                    customerExistence = self.checkCustomerExistence(str(choiceCustomer))
                    if customerExistence == False: return
                    print("\nCustomer ID:", str(choiceCustomer))
                    for customerID in self.customerDatabase[str(choiceCustomer)]:
                        print("   ", customerID, self.customerDatabase[str(choiceCustomer)][customerID])
                elif choiceCustomerDatabase == 3:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
                    
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not a number. Please try again.") 
            
    def showCustomerDatabase(self):
        print("\nCUSTOMER DATABASE")
        for CustomerID, CustomerInformation in self.customerDatabase.items():
            print("Customer ID:", CustomerID)
            for keyInfo in CustomerInformation:
                print("   ", keyInfo, CustomerInformation[keyInfo]) 
                
    def displayBankMonetaryCollection(self):
        print("\nBANK MONETARY FUNDS")
        for id, amount in self.bankMonetaryCollection.items():
            print(id, amount) 
        
    def customerJsonToDict(self):
        try:
            with open("Database/CustomerDatabase.json") as customerDatabaseJSON:
                self.customerDatabase = json.load(customerDatabaseJSON)
            
            customerDatabaseJSON.close()
        except:
            pass
            
    def addToCustomerJsonFile(self):
        try:
            with open("Database/CustomerDatabase.json", "w") as customerDatabaseJSON:
                json.dump(self.customerDatabase, customerDatabaseJSON)
                
            customerDatabaseJSON.close()
        except FileNotFoundError as e:
            print(e)
            print("File not found.")
            
    def bankMonetaryJsonToDict(self):
        try:
            with open("Database/BankMonetaryCollection.json") as bankMonetaryDatabaseJSON:
                self.bankMonetaryCollection = json.load(bankMonetaryDatabaseJSON)
            
            bankMonetaryDatabaseJSON.close()
        except:
            self.bankMonetaryCollection["Bank Balance:"] = 0.0
            self.bankMonetaryCollection["Mint Total:"] = 0.0
            self.bankMonetaryCollection["Burn Total:"] = 0.0
            self.bankMonetaryCollection["Initial Deposit Total:"] = 0.0
            
    def addToBankMonetaryJsonFile(self):
        try:
            with open("Database/BankMonetaryCollection.json", "w") as bankMonetaryDatabaseJSON:
                json.dump(self.bankMonetaryCollection, bankMonetaryDatabaseJSON)
                
            bankMonetaryDatabaseJSON.close()
        except FileNotFoundError as e:
            print(e)
            print("File not found.")
            
    def customerNewID(self):
        if "1001" in self.customerDatabase.keys():
            for dictID in reversed(self.customerDatabase.keys()):
                newID = int(dictID)
                return newID + 1
        else:
            return 1001
        
    def customerNewAccNum(self):
        if "1001" in self.customerDatabase.keys():
             for dictID in reversed(self.customerDatabase.keys()):
                newAccNum = int(self.customerDatabase[dictID]["Account Number:"])
                return newAccNum + 1 
        else:
                return 69347501  
            
    def checkCustomerExistence(self, customerTestID = 0):
        customerTestID = str(customerTestID)
        if customerTestID in self.customerDatabase.keys():
            return True
        else:
            print(f"\nCustomer {customerTestID} does not exist!")
            return False
    
    def initialDepositAcc(self):
       while True:
            initialDeposit = float(input("Enter your initial deposit: "))
            if initialDeposit <= 0 : 
                print("\nInvalid Input. Please try again")
            else:
                return initialDeposit
        
    def customerLoanInterestRate(self, creditLevelTest = 0):
        interestRateOfAccount = {2: 0.25, 3: 0.225, 4: 0.20}
        return interestRateOfAccount.get(creditLevelTest)