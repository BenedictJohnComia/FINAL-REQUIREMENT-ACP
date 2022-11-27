def Welcome():
    print("\n--------------Welcome to Granny's Banking System!--------------")
    
    while True:
        try:
            print("\nAre you an admin or a customer?")
            print("[1] Admin")
            print("[2] Customer")
            print("[3] Exit")
            choiceOfUser = int(input("Enter your choice: "))
            if choiceOfUser == 1 or choiceOfUser == 2 or choiceOfUser == 3:
                return choiceOfUser
            else:
                print("\nInvalid Input. Please try again.")
                
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
        