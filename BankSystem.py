from MainMenuMethods import MainMenuVerifyInfo, MainMenuLoanAssessment
import collections
import json

class bankSystem:
    def __init__(self):
        self.bankBalance = 0.0
        self.customerDatabase = collections.defaultdict(dict)
        self.jsonToDict()
        self.customerID = int(self.customerNewID()) 
        self.accountNumber = 69347501
        self.activityLog = []
        self.mintCount = 5
        
    def mintMoney(self):
        print("The minting limit is currently at Php 50,000.00")
        print(f"You have {self.mintCount} mints left.")
        if self.mintCount <= 5 and self.mintCount >= 1:
            addMoney = float(input("Enter amount to be minted: "))
            if addMoney < 0 or addMoney > 50000.00:
                print("Invalid Input. Please try again")
                return
            self.bankBalance = self.bankBalance + addMoney
            self.mintCount = self.mintCount - 1
            print(f"The current balance is {self.bankBalance}") 
        else:
            print("You reached the max limit for minting money today.")
        
    def burnMoney(self):
        if self.bankBalance == 0:
            print("There are no funds to be burned.")
        else:
            burnMoney = float(input("Enter amount to be burned: "))
            self.bankBalance = self.bankBalance - burnMoney
            print(f"The current balance is {self.bankBalance}") 

    def openAccount(self):
        print(f"Enter information for customer {self.customerID}")
        firstName = str(input("Enter first name: "))
        lastName = str(input("Enter last name: "))
        age = int(input("Enter age: "))
        address = str(input("Enter address: "))
        pin = int(input("Enter pin: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        balance = float(input("Enter your initial deposit: "))
        creditLevel = int(self.creditLevel())
        creditTier = str(self.creditTierTest(creditLevel))
        loanLimitAcc = float(self.loanLimit(creditLevel))
        loan = 0
        
        while True:
            print("\nPlease verify the following information:")
            print(f"{self.customerID} is {firstName} {lastName}, {age} years old from {address}, has initial deposit amounting to {balance}.")
            print(f"The pin code of customer {self.customerID} is {pin} that has:")
            print(f"Account Number : {self.accountNumber}")
            print(f"Credit Tier: {creditTier}")
            print(f"Loan Limit: {loanLimitAcc}")
            print(f"Username: {username}")
            print(f"Password: {password}\n")
            print("[1] Yes, that is correct")
            print("[2] No, I want to change some information")
            choiceVerify = int(input("Enter your choice: "))
            if choiceVerify == 2:
                MainMenuVerifyInfo()
                while True:
                    choiceChange = int(input("Enter your choice: "))
                    if choiceChange == 1:
                        firstName = str(input("Enter first name: "))
                        break
                    elif choiceChange == 2:
                        lastName = str(input("Enter last name: "))
                        break
                    elif choiceChange == 3:
                        age = int(input("Enter age: "))
                        break
                    elif choiceChange == 4:
                        address = str(input("Enter address: "))
                        break
                    elif choiceChange == 5:
                        pin = int(input("Enter pin: "))
                        break
                    elif choiceChange == 6:
                        username = input("Enter username: ")
                        break
                    elif choiceChange == 7:
                        password = input("Enter password: ")
                        break
                    elif choiceChange == 8:
                        balance = input("Enter initial deposit: ")
                        break
                    else:
                        print("Invalid Input. Please try again.")
                        
            elif choiceVerify == 1:
                self.customerDatabase[self.customerID] = {}
                self.customerDatabase[self.customerID]["First Name:"] = firstName
                self.customerDatabase[self.customerID]["Last Name:"] = lastName
                self.customerDatabase[self.customerID]["Age:"] = age
                self.customerDatabase[self.customerID]["Address:"] = address
                self.customerDatabase[self.customerID]["Account Numer:"] = self.accountNumber
                self.customerDatabase[self.customerID]["Pin:"] = pin
                self.customerDatabase[self.customerID]["Username:"] = username
                self.customerDatabase[self.customerID]["Password:"] = password
                self.customerDatabase[self.customerID]["Balance:"] = balance
                self.customerDatabase[self.customerID]["Credit Level:"] = creditLevel
                self.customerDatabase[self.customerID]["Loan Limit:"] = loanLimitAcc
                self.customerDatabase[self.customerID]["Loan:"] = loan
                break
            else:
                print("Invalid Input. Please try again.")
    
        self.bankBalance = self.bankBalance + balance
        self.customerID = self.customerID + 1
        self.accountNumber = self.accountNumber + 1
        
        self.addToCustomerJsonFile()
        
    def displayTest(self):
        choiceID = str(input("Enter customer ID to be found: "))
        print(self.customerDatabase[choiceID]["Balance:"])
        
    def jsonToDict(self):
        try:
            with open("Database/CustomerDatabase.json") as customerDatabaseJSON:
                self.customerDatabase = json.load(customerDatabaseJSON)
        except:
            self.customerDatabase[1001] = {}
            
    def customerNewID(self):
        for dictID in reversed(self.customerDatabase.keys()):
            if dictID == 1001:
                return 1001
            else:
                newID = int(dictID)
                return newID + 1
        
    def addToCustomerJsonFile(self):
        with open("Database/CustomerDatabase.json", "w") as customerJsonFile:
            json.dump(self.customerDatabase, customerJsonFile)
            
        customerJsonFile.close()
        
    def loanAssesment(self):
        MainMenuLoanAssessment()
        choiceLoanAssessment = int(input("Enter your choice: "))
        if choiceLoanAssessment == 1:
            choiceCustomer = str(input("Enter ID of customer: "))
            
        #prompt, create loan, loan payment
            #create  loan - choose customer, if tier 1 = bawal loan, if tier 2 and above = pwede mag loan depending sa limit
                #ask how much iloloan
                #loan amount + interest anf istostore sa loan vale nya sa dictionary(overwrite)
                #show aggreement with details on how much loan and how much to pay
            #loan payment - call customer ID, check if may loan
                #acces loan, check if 0, no loan
                #if 1 - may loan
    
    def accessCustomerDatabase(self):
        #show customer database
        #can search by ID
        print("tanginamo")
          
        
    def creditLevel(self):
        while True:
            creditScore = int(input("Enter credit score(0-100): "))
            if creditScore >= 0 and creditScore <= 25:
                return 1
            elif creditScore >= 26 and creditScore <= 50:
                return 2
            elif creditScore >= 51 and creditScore <= 75:
                return 3
            elif creditScore >= 75 and creditScore <= 100:
                return 4
            else:
                print("Invalid Input. Please try again")
                break
            
    def creditTierTest(self, creditLevelTest = 0):
        if creditLevelTest == 1:
            return "No Tier"
        elif creditLevelTest == 2:
            return "Bronze Tier"
        elif creditLevelTest == 3:
            return "Silver Tier"
        else:
            return "Gold Tier"
    
    def loanLimit(self, creditLevelTest = 0):
        if creditLevelTest == 1:
            return 0
        elif creditLevelTest == 2:
            return 5000
        elif creditLevelTest == 3:
            return 10000
        else:
            return 50000
        
class customerSystem(bankSystem):
    def __init__(self):
        super().__init__()
        self.brokerageBalance = 0
        self.brokerAssetDatabase = {}
    def mintMoney():
        #add
        print("tanginamo")
    
    def burnMoney():
        #decrease
        print("sdada")