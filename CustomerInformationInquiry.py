class customerInfo:
    def __init__(self):
        self.customerID = 0
        self.firstName = str(input("Enter first name: "))
        self.lastName = str(input("Enter last name: "))
        self.age = int(input("Enter age: "))
        self.address = str(input("Enter address: "))
        self.pin = int(input("Enter pin: "))
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.balance = float(input("Enter your initial deposit: "))
        self.accountNumber = 0
        self.creditLevel = 0
        self.creditTier = ""
        self.loanLimitAcc = 0
        self.loan = 0
    
    def displayInfo(self):
        print(f"Customer {self.customerID} is {self.firstName} {self.lastName}, {self.age} years old from {self.address}, has initial deposit amounting to {self.balance}.")
        print(f"The pin code of customer {self.customerID} is {self.pin} that has:")
        print(f"Account Number : {self.accountNumber}")
        print(f"Credit Tier: {self.creditTier}")
        print(f"Loan Limit: {self.loanLimitAcc}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}\n")