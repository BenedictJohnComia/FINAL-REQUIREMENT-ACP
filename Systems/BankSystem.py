from MainMenuMethods import MainMenuVerifyInfo, MainMenuCustomerDatabase
from Systems.CustomerInformationInquiry import customerInfo
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
        self.bankBalance = self.bankMonetaryCollection["Bank Balance"]
        self.mintTotal = self.bankMonetaryCollection["Mint Total"]
        self.burnTotal = self.bankMonetaryCollection["Burn Total"]
        self.initialDepositTotal = self.bankMonetaryCollection["Initial Deposit Total"]
        self.loanTotal = self.bankMonetaryCollection["Loan Total"]
        self.mintCount = 5
     
    def addMoney(self):
        try:
            self.bankMonetaryJsonToDict()
            print("\nMINT MONEY")
            print("The minting limit is currently at ₱50,000.00")
            print(f"You have {self.mintCount} mints left.")
            if self.mintCount <= 5 and self.mintCount >= 1:
                addMoney = float(input("Enter amount to be minted: "))
                if addMoney < 0 or addMoney > 50000.00:
                    print("\nInvalid Input. Please try again.")
                    return
                
                self.mintCount = self.mintCount - 1
                self.mintTotal = self.mintTotal + addMoney
                self.bankBalance = self.bankBalance + addMoney
                self.bankMonetaryCollection["Mint Total"] = self.mintTotal
                self.bankMonetaryCollection["Bank Balance"] = self.bankBalance
                
                print(f"\nSuccessfully minted ₱{addMoney}! ") 
                print(f"The mint total is ₱{self.mintTotal}") 
                print(f"The current balance of bank is ₱{self.bankBalance}") 
                
                self.addToBankMonetaryJsonFile()
            else:
                print("\nYou reached the max limit for minting money today.")
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not a number. Please try again.")
        
    def removeMoney(self):
        try:
            self.bankMonetaryJsonToDict()
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
                self.bankMonetaryCollection["Burn Total"] = self.burnTotal
                self.bankMonetaryCollection["Bank Balance"] = self.bankBalance
                
                print(f"\nSuccessfully burned ₱{burnMoney}! ")
                print(f"The burn total is ₱{self.burnTotal}") 
                print(f"The current balance is ₱{self.bankBalance}") 
                
                self.addToBankMonetaryJsonFile()
                
        except ValueError as e:
            print("\nThe program", e)
            print ("You entered a value that is not a number. Please try again.")
        
    def openAccount(self):
        try:
            self.customerJsonToDict()
            self.customerID = str(self.customerNewID())
            self.accountNumber = int(self.customerNewAccNum())
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
                    self.customerDatabase[self.customerID]["First Name"] =  customerObj.firstName
                    self.customerDatabase[self.customerID]["Last Name"] = customerObj.lastName
                    self.customerDatabase[self.customerID]["Age"] = customerObj.age
                    self.customerDatabase[self.customerID]["Sexual Identity"] = customerObj.sexualIdentity
                    self.customerDatabase[self.customerID]["Address"] = customerObj.address
                    self.customerDatabase[self.customerID]["Account Number"] = customerObj.accountNumber
                    self.customerDatabase[self.customerID]["Pin"] = customerObj.pin
                    self.customerDatabase[self.customerID]["Username"] = customerObj.username
                    self.customerDatabase[self.customerID]["Password"] = customerObj.password
                    self.customerDatabase[self.customerID]["Balance"] = customerObj.balance
                    self.customerDatabase[self.customerID]["Credit Level"] = customerObj.creditLevelofCustomer
                    self.customerDatabase[self.customerID]["Loan Limit"] = customerObj.loanLimitAcc
                    self.customerDatabase[self.customerID]["Loan"] = customerObj.loan
                    
                    self.initialDepositTotal = self.initialDepositTotal + customerObj.balance
                    self.bankBalance = self.bankBalance + customerObj.balance
                    self.bankMonetaryCollection["Initial Deposit Total"] = self.initialDepositTotal
                    self.bankMonetaryCollection["Bank Balance"] = self.bankBalance
                    print(f"\nThe initial deposit total is ₱{self.initialDepositTotal}") 
                    print(f"The current balance of bank is ₱{self.bankBalance}") 
                    
                    self.addToCustomerJsonFile()
                    self.addToBankMonetaryJsonFile()
                    break
                
                else:
                    print("Invalid Input. Please try again.")
            
        except ValueError as e:
            print("\nThe program determined an", e)
            print ("You entered a value that is not an integer. Please try again.")
        except TypeError as e:
            print("\nThe", e)
            print ("An invalid input caused this error")
        except AttributeError as e:
            print("\nThe", e)
            print ("An invalid input caused this error")
            
    def loanAssesment(self):
        try:
            self.bankMonetaryJsonToDict()
            self.customerJsonToDict()
            
            print("\nLOAN ASSESSMENT")
            choiceCustomer = int(input("Enter ID of customer: "))
            customerExistence = self.checkCustomerExistence(choiceCustomer)
            if customerExistence == False: return
            
            choiceCustomer = str(choiceCustomer)
            customerCreditLevel = int(self.customerDatabase[choiceCustomer]["Credit Level"])
            customerLoan =  float(self.customerDatabase[choiceCustomer]["Loan"])
            customerLoanLimit = float(self.customerDatabase[choiceCustomer]["Loan Limit"])
            customerLoanInterestRate = self.customerLoanInterestRate(customerCreditLevel)
            print(f"\nCustomer {choiceCustomer} currently has a loan amounting to ₱{customerLoan}.")
            print(f"The loan limit of Customer {choiceCustomer} is ₱{customerLoanLimit}.")
            
            if customerCreditLevel == 1:
                print(f"Customer {choiceCustomer} cannot loan in the bank because he/she has No Tier.")
                return
            else:
                self.bankBalance = self.bankMonetaryCollection["Bank Balance"]
                print(f"Bank Balance: {self.bankBalance}")
                loanAmount = float(input("How much money will be loaned: "))
                if loanAmount > self.bankBalance:
                    print(f"\nYou entered an amount that exceeds the bank balance.")
                elif loanAmount > customerLoanLimit:
                    print(f"\nYou entered an amount that exceeds the loan limit of Customer {choiceCustomer}")
                elif loanAmount <= 0:
                    print(f"\nYou entered an invalid amount")
                else:
                    currentLoan = self.customerDatabase[choiceCustomer]["Loan"]
                    loanWithInterest = (loanAmount + (customerLoanInterestRate * loanAmount)) + currentLoan
                    if loanWithInterest > customerLoanLimit:
                        print(f"\nThe current loan exceeds the loan limit which is ₱{customerLoanLimit}")
                        print("Sorry for the inconvenience. Please try again.")
                    else:
                        print("\nThe following transactions are made: ")
                        print(f"Loan placed: ₱{loanAmount}")
                        print(f"Loan to be payed (with annual interest): ₱{loanWithInterest}")
                        
                        self.bankMonetaryCollection["Bank Balance"] = float(self.bankMonetaryCollection["Bank Balance"] - loanAmount)
                        self.loanTotal = self.bankMonetaryCollection["Loan Total"]
                        self.bankMonetaryCollection["Loan Total"] = float(self.loanTotal + loanAmount)
                        self.customerDatabase[choiceCustomer]["Loan"] = float(loanWithInterest)
                        
                        self.addToCustomerJsonFile()
                        self.addToBankMonetaryJsonFile()
                        self.bankMonetaryJsonToDict()
                        self.customerJsonToDict()
          
        except ValueError as e:
            print("\nThe program determined an", e)
            print ("You entered a value that is not a number. Please try again.") 
    
    def closeAccount(self):
        try:
            self.customerJsonToDict()
            self.bankMonetaryJsonToDict()
            
            print("\nCLOSE ACCOUNT")
            choiceCustomer = int(input("Enter ID of customer: "))
            customerExistence = self.checkCustomerExistence(choiceCustomer)
            customerLoan =  float(self.customerDatabase[str(choiceCustomer)]["Loan"])
            if customerExistence == False: return
            
            print("\nCustomer ID :", str(choiceCustomer))
            for customerID in self.customerDatabase[str(choiceCustomer)]:
                print("   ", customerID, ":", self.customerDatabase[str(choiceCustomer)][customerID])
            
            if customerLoan > 0.0:
                print(f"\nCustomer {choiceCustomer} currently has a loan amounting to ₱{customerLoan}.")
                print(f"Account cannot be closed when there is still a loan in the account.")
                return
                
            while True:
                print(f"\nAre you sure you want to close the account of Customer {choiceCustomer} ?")
                print("[1] Yes")
                print("[2] No")
                choiceClose = int(input("Enter your choice: "))
                if choiceClose == 1:
                    self.bankMonetaryCollection["Bank Balance"] = float(self.bankMonetaryCollection["Bank Balance"] - self.customerDatabase[str(choiceCustomer)]["Balance"])
                    del self.customerDatabase[str(choiceCustomer)]
                    
                    print(f"\nThe account of Customer {choiceCustomer} is succesfully closed.")
                    
                    self.addToBankMonetaryJsonFile()
                    self.bankMonetaryJsonToDict()
                    self.addToCustomerJsonFile()
                    self.customerJsonToDict()
                    break
                elif choiceClose == 2:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
                    
        except ValueError as e:
            print("\nThe program determined an", e)
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
                    customerExistence = self.checkCustomerExistence(choiceCustomer)
                    if customerExistence == False: return
                    print("\nCustomer ID :", str(choiceCustomer))
                    for customerID in self.customerDatabase[str(choiceCustomer)]:
                        print("   ", customerID, ":", self.customerDatabase[str(choiceCustomer)][customerID])
                elif choiceCustomerDatabase == 3:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
                    
        except ValueError as e:
            print("\nThe program determined an", e)
            print ("You entered a value that is not a number. Please try again.") 
            
    def showCustomerDatabase(self):
        self.customerJsonToDict()
        print("\nCUSTOMER DATABASE")
        print("--------------------------------------------")
        for CustomerID, CustomerInformation in self.customerDatabase.items():
            print("\nCustomer ID :", CustomerID)
            for keyInfo in CustomerInformation:
                print("   ", keyInfo, ":", CustomerInformation[keyInfo]) 
        print("--------------------------------------------")      
         
    def displayBankMonetaryCollection(self):
        print("\nBANK MONETARY FUNDS")
        for id, amount in self.bankMonetaryCollection.items():
            print(id, "₱", amount) 
        
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
                orderedDict = collections.OrderedDict(sorted(self.customerDatabase.items()))
                json.dump(orderedDict, customerDatabaseJSON, indent = 4)
                
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
            self.bankMonetaryCollection["Bank Balance"] = 0.0
            self.bankMonetaryCollection["Mint Total"] = 0.0
            self.bankMonetaryCollection["Burn Total"] = 0.0
            self.bankMonetaryCollection["Initial Deposit Total"] = 0.0
            self.bankMonetaryCollection["Loan Total"] = 0.0
            
    def addToBankMonetaryJsonFile(self):
        try:
            with open("Database/BankMonetaryCollection.json", "w") as bankMonetaryDatabaseJSON:
                json.dump(self.bankMonetaryCollection, bankMonetaryDatabaseJSON, indent = 4)
                
            bankMonetaryDatabaseJSON.close()
            
        except FileNotFoundError as e:
            print(e)
            print("File not found.")
            
    def customerNewID(self):
        if "1001" in self.customerDatabase.keys():
            for dictID in self.customerDatabase.keys():
                currentID = int(dictID)
                testID = currentID - 1
                if testID == 1000:
                    continue
                elif str(testID) not in self.customerDatabase.keys():
                    return int(testID)
                elif str(currentID + 1) in self.customerDatabase.keys():
                    continue
            else:
                newID = currentID + 1
                return int(newID)
        else:
            return 1001
        
    def customerNewAccNum(self):
        if "1001" in self.customerDatabase.keys():
            for dictID in self.customerDatabase.keys():
                currentAccNum = int((self.customerDatabase[dictID]["Account Number"]))
                testAccNum = currentAccNum - 1
                currentID = int(dictID)
                testID = currentID - 1
                if testID == 1000:
                    continue
                elif str(testID) not in self.customerDatabase.keys():
                    return int(testAccNum)
                elif str(currentID + 1) in self.customerDatabase.keys():
                    continue
            else:
                newAccNum = currentAccNum + 1
                return int(newAccNum)
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