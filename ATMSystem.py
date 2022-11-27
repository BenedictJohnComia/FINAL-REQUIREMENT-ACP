from BankSystem import bankSystem
from CustomerLogin import customerLogin
from MainMenuMethods import MainMenuCustomer
import collections
import json

class atmSystem(bankSystem):
    def __init__(self, customerID):
        self.customerJsonToDict()
        self.bankMonetaryJsonToDict()
        self.CustomerInfo  = collections(dict)
        self.customerID = customerID
    
    