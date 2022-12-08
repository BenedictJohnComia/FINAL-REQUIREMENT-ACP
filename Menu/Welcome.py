from Menu.MainMenuMethods import MainMenuYesOrNo

def Welcome():
    print("\n--------------Welcome to Granny's Banking System!--------------")
    
    while True:
        try:
            print("\nAre you an admin or a customer?")
            print("   [1] Admin")
            print("   [2] Customer")
            print("   [3] Exit")
            choiceOfUser = int(input("Enter your choice: "))
            if choiceOfUser == 1 or choiceOfUser == 2 :
                return choiceOfUser
            elif choiceOfUser == 3:
                while True:
                    print("\nAre you sure you want to exit?")
                    MainMenuYesOrNo()
                    choiceYesNo = int(input("Enter choice: "))
                    if choiceYesNo == 1:
                        print("\nThank you for using the Granny's Banking System. Have a nice day!")
                        return choiceOfUser
                    elif choiceYesNo == 2:
                        break
                    else:
                        print("\nInvalid Input. Please try again.")
            else:
                print("\nInvalid Input. Please try again.")
                
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
        