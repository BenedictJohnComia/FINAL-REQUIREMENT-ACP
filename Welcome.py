def Welcome():
    username = input("Greetings! You are? ")
    print("Welcome to Granny's Banking System Mr/Ms.", username)
    print("==============================================")
    
    while True:
        try:
            print("\nAre you an admin or a customer?")
            print("[1] Admin")
            print("[2] Customer")
            choiceOfUser = int(input("\nEnter your choice: "))
            if choiceOfUser == 1:
                return choiceOfUser
            elif choiceOfUser == 2:
                return choiceOfUser
            else:
                print("\nInvalid Input. Please try again.")
                
        except ValueError as e:
            print("\nThe program receives an", e)
            print ("You entered a value that is not a number. Please try again.")
        