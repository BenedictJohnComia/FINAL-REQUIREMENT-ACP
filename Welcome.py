def Welcome():
    username = input("Greetings! You are? ")
    print("\nWelcome to Granny's Banking System Mr/Ms.", username)
    print("==============================================")
    print("\nAre you an admin or a broker?")
    print("\n\t[1] Admin")
    print("\t[2] Broker")
    
    while True:
        choiceOfUser = int(input("\nEnter your choice: "))
        if choiceOfUser == 1:
            return choiceOfUser
        elif choiceOfUser == 2:
            return choiceOfUser
        else:
            print("Invalid Input. Please try again.")
            