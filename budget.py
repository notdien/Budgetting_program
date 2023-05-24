# refracting code in a Object-Orientated style
class Account():
    # constructor with attributes of a user's account
    # the attributes of a user's account should have the balance
    # creating three different balances since we want to have a needs, wants and savings
    def __init__(self, needs, wants, savings):
        self.needs = needs
        self.wants = wants
        self.savings = savings

    # a method to add

    # a method to subtract

    # method to provide information
    def __repr__(self):
        return f"Balance for account:\nNeeds: ${self.needs}, Wants: ${self.wants}, Savings: ${self.savings}"


# defining a new user account
diens_account = Account(100, 50, 300)
print(diens_account)
