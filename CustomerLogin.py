from AdminLogin import adminLogin
import json
import collections

class customerLogin(adminLogin):
    def __init__(self):
        self.customerDatabase = collections.defaultdict(dict)
        self.customerJsonToDict()
        self.adminID = int(self.adminNewID())
        self.adminUsername = ""
        self.adminPassword = ""
        
    def login(self):
        self.adminJsonToDict()
        
        adminLoginID = int(input("Enter your Admin ID: "))
        adminExistence = self.checkExistence(adminLoginID)
        if adminExistence == False: return
        
        self.adminUsername = self.adminDatabase[str(adminLoginID)]["Username"]
        self.adminPassword = self.adminDatabase[str(adminLoginID)]["Password"]
        
        while True:
            adminLoginUsername = str(input("Enter your username: "))
            adminLoginPassword = str(input("Enter your password: "))
            if self.adminUsername == adminLoginUsername and self.adminPassword == adminLoginPassword:
                print("\nLogin Successful!")
                print(f"Welcome Admin {adminLoginID}!")
                return 1
            else:
                print("\nIncorrect Username or Password. Please try again.\n")
                  
    def register(self):
        self.adminJsonToDict()
        self.adminID = str(self.adminNewID())
        
        print(f"\nEnter the information for Admin {self.adminID}:")
        adminRegisterUsername = str(input("Enter your username: "))
        adminRegisterPassword = str(input("Enter your password: "))
        
        self.adminDatabase[self.adminID] = {}
        self.adminDatabase[self.adminID]["Username"] = adminRegisterUsername
        self.adminDatabase[self.adminID]["Password"] = adminRegisterPassword
        
        print(f"\nRegister successful for Admin {self.adminID}")
        
        self.addToAdminJsonFile()
        
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