from Login.AdminLogin import adminLogin
import json
import collections
import pwinput

class customerLogin(adminLogin):
    def __init__(self):
        self.customerDatabase = collections.defaultdict(dict)
        self.customerFirstName = ""
        self.customerLastName = ""
        self.customerUsername = ""
        self.customerPassword = ""
        self.loginCount = 3
        
    def login(self):
        try:
            while True:
                self.customerJsonToDict()
                self.accountNumber = int(input("\nEnter your account number: "))
                self.customerID = int(self.getCustomerID(self.accountNumber))
                if self.customerID == 0: return 0
                
                self.customerUsername = self.customerDatabase[str(self.customerID)]["Username"]
                self.customerPassword = self.customerDatabase[str(self.customerID)]["Password"]
                self.customerFirstName = self.customerDatabase[str(self.customerID)]["First Name"]
                self.customerLastName = self.customerDatabase[str(self.customerID)]["Last Name"]
                while True:
                    customerLoginUsername = str(input("Enter your username: "))
                    customerLoginPassword = str(pwinput.pwinput(prompt = "Enter your password: ", mask = "*"))
                    if self.customerUsername == customerLoginUsername and self.customerPassword == customerLoginPassword:
                        print("\nLogin Successful!")
                        print(f"Welcome {self.customerFirstName} {self.customerLastName}!")
                        return 2
                    else:
                        pinCount = self.pinCount()
                        if pinCount == False: return 0
                        
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
            
    def checkExistence(self, customerTestID = 0):
        customerTestID = str( customerTestID)
        if customerTestID in self.customerDatabase.keys():
            return True
        else:
            print(f"\nCustomer {customerTestID} does not exist!")
            return False
    
    def customerJsonToDict(self):
        try:
            with open("Database/CustomerDatabase.json") as customerDatabaseJSON:
                self.customerDatabase = json.load(customerDatabaseJSON)
            
            customerDatabaseJSON.close()
        except:
            pass
    
    def getCustomerID(self, accNumber = 0):
        for keyOfDict, valOfDict in self.customerDatabase.items():
            for nestedKey, nestedVal in valOfDict.items():
                if accNumber == nestedVal:
                    return keyOfDict
        else:
            print(f"\nAccount number {accNumber} does not exist!")
            return 0