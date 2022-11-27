from Welcome import Welcome
from MainMenuMethods import MainMenuAdmin, MainMenuCustomer, MainMenuLoginAdmin, MainMenuLoginCustomer
from BankSystem import bankSystem
from ATMSystem import atmSystem
from AdminLogin import adminLogin
from CustomerLogin import customerLogin

mainBank = bankSystem()
adminLoginObj = adminLogin()
customerLoginObj = customerLogin()
systemUser = 0

while True:
    choiceOfUser = Welcome()
    if choiceOfUser == 1: 
        while True:
            try:
                MainMenuLoginAdmin()
                choiceAdminLogin = int(input("Enter choice: "))
                if choiceAdminLogin == 1:
                    systemUser = adminLoginObj.login()
                    if systemUser == 1:
                        break
                elif choiceAdminLogin == 2:
                    adminLoginObj.register()
                elif choiceAdminLogin == 3:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
                    
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")
                
    elif choiceOfUser == 2:
        while True:
            try:
                MainMenuLoginCustomer()
                choiceCustomerLogin = int(input("Enter choice: "))
                if choiceCustomerLogin == 1:
                    systemUser = customerLoginObj.login()
                    if systemUser == 2:
                        break
                elif choiceCustomerLogin == 2:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
        
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")
                
    if systemUser == 1: 
        while True:
            try:
                MainMenuAdmin()
                userInput = int(input("Enter choice: "))
                if userInput == 1:
                    mainBank.addMoney()
                elif userInput == 2:
                    mainBank.removeMoney()
                elif userInput == 3:
                    mainBank.openAccount()
                elif userInput == 4:
                    mainBank.loanAssesment()
                elif userInput == 5:
                    mainBank.closeAccount()
                elif userInput == 6:
                    mainBank.accessCustomerDatabase()
                elif userInput == 7:
                    mainBank.displayBankMonetaryCollection()
                elif userInput == 8:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
            
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")

    elif systemUser == 2:
        while True:
            try:
                MainMenuCustomer()
                atm = atmSystem(customerLoginObj.customerID)
                userInput = int(input("Enter choice: "))
                if userInput == 1:
                    atm.addMoney()
                elif userInput == 2:
                    atm.removeMoney()
                elif userInput == 3:
                    atm.payLoan()
                elif userInput == 4:
                    atm.checkBalance()
                elif userInput == 5:
                    break
                else:
                    print("\nInvalid Input. Please try again.")
            
            except ValueError as e:
                print("\nThe program receives an", e)
                print ("You entered a value that is not a number. Please try again.")
