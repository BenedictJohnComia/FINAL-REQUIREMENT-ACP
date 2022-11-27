from Login.AdminLogin import adminLogin
import json
import collections

class customerLogin(adminLogin):
    def __init__(self):
        self.customerDatabase = collections.defaultdict(dict)
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
                
                self.customerUsername = self.customerDatabase[str(self.customerID)]["Username:"]
                self.customerPassword = self.customerDatabase[str(self.customerID)]["Password:"]

                while True:
                    customerLoginUsername = str(input("Enter your username: "))
                    customerLoginPassword = str(input("Enter your password: "))
                    
                    if self.customerUsername == customerLoginUsername and self.customerPassword == customerLoginPassword:
                        print("\nLogin Successful!")
                        print(f"Welcome Customer {self.customerID}!")
                        return 2
                    else:
                        pinCount = self.pinCount()
                        if pinCount == False: return 0
                        
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
            
    def checkExistence(self, adminTestID = 0):
        adminTestID = str(adminTestID)
        if adminTestID in self.adminDatabase.keys():
            return True
        else:
            print(f"\nAdmin {adminTestID} does not exist!")
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