from Welcome import Welcome
from MainMenuMethods import MainMenuAdmin, MainMenuBroker
from BankSystem import bankSystem, customerSystem

choiceOfUser = Welcome()
mainBank = bankSystem()
broker = customerSystem()
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
            mainBank.displayTest()
            #mainBank.assetDatabase()
        elif userinput == 7:
            break
        else:
            print("Invalid Input. Please try sheesh")
