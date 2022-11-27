from Welcome import Welcome
from MainMenuMethods import MainMenuAdmin, MainMenuCustomer, MainMenuLoginAdmin
from BankSystem import bankSystem
from ATMSystem import atmSystem
from AdminLogin import adminLogin

choiceOfUser = Welcome()
mainBank = bankSystem()
admin = adminLogin()
systemUser = 0

if choiceOfUser == 1: 
    while True:
        try:
            MainMenuLoginAdmin()
            choiceAdminLogin = int(input("Enter choice: "))
            if choiceAdminLogin == 1:
                systemUser = admin.login()
                break
            elif choiceAdminLogin == 2:
                admin.register()
            elif choiceAdminLogin == 3:
                break
            else:
                print("\nInvalid Input. Please try again")
                
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
            
elif choiceOfUser == 2:
    while True:
        try:
            MainMenuLoginAdmin()
            atmObj = atmSystem()
            choiceAdminLogin = int(input("Enter choice: "))
            if choiceAdminLogin == 1:
                systemUser = admin.login()
                break
            elif choiceAdminLogin == 2:
                admin.register()
            elif choiceAdminLogin == 3:
                break
            else:
                print("\nInvalid Input. Please try again")
                
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
            
if systemUser == 1: 
    while True:
        try:
            MainMenuAdmin()
            userinput = int(input("Enter choice: "))
            if userinput == 1:
                mainBank.mintMoney()
            elif userinput == 2:
                mainBank.burnMoney()
            elif userinput == 3:
                mainBank.openAccount()
            elif userinput == 4:
                mainBank.loanAssesment()
            elif userinput == 5:
                mainBank.closeAccount()
            elif userinput == 6:
                mainBank.accessCustomerDatabase()
            elif userinput == 7:
                mainBank.displayBankMonetaryCollection()
            elif userinput == 8:
                break
            else:
                print("\nInvalid Input. Please try again")
        
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")