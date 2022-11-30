class customerInfo:
    def __init__(self):
        self.customerID = 0
        self.accountNumber = 0
        self.firstName = str(input("Enter first name: "))
        self.lastName = str(input("Enter last name: "))
        self.age = int(input("Enter age: "))
        self.sex = str(self.sexualIdentity())
        self.address = str(input("Enter address: "))
        self.pin = int(input("Enter pin: "))
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.balance = 0.0
        self.creditLevelofCustomer = int(self.creditLevel())
        self.creditTier = str(self.creditTierTest(self.creditLevelofCustomer))
        self.loanLimitAcc = float(self.loanLimit(self.creditLevelofCustomer))
        self.loan = 0
    
    def displayInfo(self):
        print("\nPlease verify the following information:")
        print(f"Customer {self.customerID} is {self.firstName} {self.lastName}, {self.age} years old from {self.address}, has initial deposit amounting to ₱{self.balance}.")
        print(f"Account Number: {self.accountNumber}")
        print(f"Pin: {self.pin}")
        print(f"Credit Tier: {self.creditTier}")
        print(f"Loan Limit: {self.loanLimitAcc}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}\n")
    
    def creditLevel(self):
        while True:
            creditScore = int(input("Enter credit score(0-100): "))
            if creditScore >= 0 and creditScore <= 25:
                return 1
            elif creditScore >= 26 and creditScore <= 50:
                return 2
            elif creditScore >= 51 and creditScore <= 75:
                return 3
            elif creditScore >= 75 and creditScore <= 100:
                return 4
            else:
                print("Invalid Input. Please try again")
                break
            
    def creditTierTest(self, creditLevelTest = 0):
        tierOfAccount = {1: "No Tier", 2: "Bronze Tier", 3: "Silver Tier", 4: "Gold Tier"}
        return tierOfAccount.get(creditLevelTest)
    
    def loanLimit(self, creditLevelTest = 0):
        loanLimitOfAccount = {1: 0, 2: 5000, 3: 10000, 4: 50000}
        return loanLimitOfAccount.get(creditLevelTest)
    
    def sexualIdentity(self):
        sexualIdentity = {1: "Male", 2: "Female"}
        while True:
            print("Sex:\n   [1] - Male\n   [2] - Female")
            sex = int(input("Enter your choice: "))
            if sex == 1 or sex == 2:
                return sexualIdentity.get(sex)
            else:
                print("\nInvalid Input. Please try again\n")
        