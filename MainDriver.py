from Welcome import Welcome
from MainMenuMethods import MainMenuAdmin, MainMenuCustomer
from BankSystem import bankSystem

choiceOfUser = Welcome()
mainBank = bankSystem()
if choiceOfUser == 1: 
    while True:
        MainMenuAdmin()
        userinput = int(input("ENTER CHOICE: "))
        if userinput == 1:
            mainBank.mintMoney()
        elif userinput == 2:
            mainBank.burnMoney()
        elif userinput == 3:
            mainBank.openAccount()
        elif userinput == 4:
            mainBank.loanAssesment()
        elif userinput == 5:
            mainBank.accessCustomerDatabase()
        elif userinput == 6:
            mainBank.displayBankMonetaryCollection()
        elif userinput == 7:
            break
        else:
            print("Invalid Input. Please try sheesh")