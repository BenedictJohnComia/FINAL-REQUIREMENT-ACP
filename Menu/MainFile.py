from Menu.Welcome import Welcome
from Menu.MainMenuMethods import MainMenuAdmin, MainMenuCustomer, MainMenuLoginAdmin, MainMenuLoginCustomer
from Systems.BankSystem import bankSystem
from Systems.ATMSystem import atmSystem
from Login.AdminLogin import adminLogin
from Login.CustomerLogin import customerLogin

class mainFile:
    def __init__(self):
        self.mainBank = bankSystem()
        self.adminLoginObj = adminLogin()
        self.customerLoginObj = customerLogin()
        self.systemUser = 0

    def welcomePrompt(self):
        while True:
            choiceOfUser = Welcome()
            if choiceOfUser == 1: 
                self.adminLogin()
            elif choiceOfUser == 2:
                self.customerLogin()
            elif choiceOfUser == 3:
                break
        
    def adminLogin(self):
        while True:
            try:
                MainMenuLoginAdmin()
                choiceAdminLogin = int(input("Enter choice: "))
                if choiceAdminLogin == 1:
                    systemUser = self.adminLoginObj.login()
                    if systemUser == 1:
                        self.bankSystem()
                elif choiceAdminLogin == 2:
                    self.adminLoginObj.register()
                elif choiceAdminLogin == 3:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
                    
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")
    
    def customerLogin(self):
        while True:
            try:
                MainMenuLoginCustomer()
                choiceCustomerLogin = int(input("Enter choice: "))
                if choiceCustomerLogin == 1:
                    systemUser = self.customerLoginObj.login()
                    if systemUser == 2:
                        self.atmSystem()
                elif choiceCustomerLogin == 2:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
        
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")                    
    
    def bankSystem(self):
        while True:
            try:
                MainMenuAdmin()
                userInput = int(input("Enter choice: "))
                if userInput == 1:
                    self.mainBank.addMoney()
                elif userInput == 2:
                    self.mainBank.removeMoney()
                elif userInput == 3:
                    self.mainBank.openAccount()
                elif userInput == 4:
                    self.mainBank.loanAssesment()
                elif userInput == 5:
                    self.mainBank.closeAccount()
                elif userInput == 6:
                    self.mainBank.accessCustomerDatabase()
                elif userInput == 7:
                    self.mainBank.displayBankMonetaryCollection()
                elif userInput == 8:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
            
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")
    
    def atmSystem(self):
        while True:
            try:
                MainMenuCustomer()
                self.atm = atmSystem(self.customerLoginObj.customerID)
                userInput = int(input("Enter choice: "))
                if userInput == 1:
                    self.atm.addMoney()
                elif userInput == 2:
                    self.atm.removeMoney()
                elif userInput == 3:
                    self.atm.payLoan()
                elif userInput == 4:
                    self.atm.checkBalance()
                elif userInput == 5:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
            
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")