import json
import collections
import pwinput

class adminLogin:
    def __init__(self):
        self.adminDatabase = collections.defaultdict(dict)
        self.adminJsonToDict()
        self.adminID = int(self.adminNewID())
        self.adminUsername = ""
        self.adminPassword = ""
        self.loginCount = 3
        
    def login(self):
        self.adminJsonToDict()
        
        adminLoginID = int(input("Enter your Admin ID: "))
        adminExistence = self.checkExistence(adminLoginID)
        if adminExistence == False: return
        
        self.adminUsername = self.adminDatabase[str(adminLoginID)]["Username"]
        self.adminPassword = self.adminDatabase[str(adminLoginID)]["Password"]
        
        while True:
            adminLoginUsername = str(input("Enter your username: "))
            adminLoginPassword = str(pwinput.pwinput(prompt = "Enter your password: ", mask = "*"))
            if self.adminUsername == adminLoginUsername and self.adminPassword == adminLoginPassword:
                print("\nLogin Successful!")
                print(f"Welcome Admin {adminLoginID}!")
                return 1
            else:
                pinCount = self.pinCount()
                if pinCount == False: return 0
                  
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
        
    def adminJsonToDict(self):
        try:
            with open("Database/AdminDatabase.json") as adminDatabaseJSON:
                self.adminDatabase = json.load(adminDatabaseJSON)
            
            adminDatabaseJSON.close()
        except:
            pass
            
    def addToAdminJsonFile(self):
        try:
            with open("Database/AdminDatabase.json", "w") as adminDatabaseJSON:
                orderedDict = collections.OrderedDict(sorted(self.adminDatabase.items()))
                json.dump(orderedDict, adminDatabaseJSON, indent = 4)
                
            adminDatabaseJSON.close()
        except FileNotFoundError as e:
            print(e)
            print("File not found.")
    
    def adminNewID(self):
        if "60381" in self.adminDatabase.keys():
            for dictID in self.adminDatabase.keys():
                currentID = int(dictID)
                testID = currentID - 1
                if testID == 60380:
                    continue
                elif str(testID) not in self.adminDatabase.keys():
                    return int(testID)
                elif str(currentID + 1) in self.adminDatabase.keys():
                    continue
            else:
                newID = currentID + 1
                return int(newID)
        else:
            return 60381
    
    def pinCount(self):
        self.loginCount = self.loginCount - 1
        print("\nIncorrect Username or Password. Please try again.")
        if self.loginCount == 0:
            print("You reached the max amount of tries. Please try again.")
            return False
        else:
            print(f"You have {self.loginCount} tries left.\n")