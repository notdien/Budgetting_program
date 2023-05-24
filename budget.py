# refracting code in a Object-Orientated style
class Account():
    # constructor with attributes of a user's account
    # the attributes of a user's account should have the balance
    # creating three different balances since we want to have a needs, wants and savings
    def __init__(self, needs, wants, savings):
        self.needs = needs
        self.wants = wants
        self.savings = savings

    # methods to add paychecks

    # method for the paycheck of the first month
    # this paycheck takes care of all the bills
    def first_paycheck(self, amount):
        amount = round(amount, 2)

        print(f"Incoming amount is: ${amount}")

        car_insurance = 160.00
        roth = 20.00
        music = 5.46
        gym = 10.51
        icloud = 1.00

        needs_p = 0.50
        wants_p = 0.30
        savings_p = 0.20

    # method for the second paycheck of the month
    # this paychecks takes care of savings

    def second_paycheck(self, amount):
        amount = round(amount, 2)

        print(f"Incoming amount is: ${amount}")

        needs_total = 100
        wants_total = 100

        self.needs += needs_total
        self.wants += wants_total

        savings_total = amount - needs_total - wants_total
        # print(savings_total)

        self.savings += savings_total

    # methods to add

    def add_needs(self, amount):
        self.needs += amount

    def add_wants(self, amount):
        self.wants += amount

    def add_savings(self, amount):
        self.savings += amount

    # methods to subtract

    def sub_needs(self, amount):
        self.needs -= amount

    def sub_wants(self, amount):
        self.wants -= amount

    def sub_savings(self, amount):
        self.savings -= amount

    # method to provide information
    def __repr__(self):
        return f"Balance for account:\nNeeds: ${self.needs}, Wants: ${self.wants}, Savings: ${self.savings}"


# defining a new user account
diens_account = Account(100, 50, 300)
print(f"Initial amount of the account - {diens_account}")
diens_account.add_needs(100)
print(diens_account)
diens_account.sub_savings(50)
print(diens_account)
