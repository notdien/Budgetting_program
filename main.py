# # automating my income split

# # option 1 - display how much money I have
# def display():
#     # Commenting this out but this is used to rewrite the file if needed!!!
#     # file_opener = open("records.txt", "w")
#     # file_opener.write('%-15s %15s %15s %15s\n' % ("Reason:", "Needs:", "Wants:", "Savings:"))
#     # file_opener.close()

#     with open("records.txt", 'r') as text:
#         for line in text:
#             print(line, end='')


# # option 2 - subtracting money
# def sub():
#     print("1) Subtract money from needs?")
#     print("2) Subtract money from wants?")
#     print("3) Subtract money from savings?")
#     sub_choice = int(input("Which one do you want to sub from(1,2 or 3):"))

#     if sub_choice == 1:
#         print("1) SUBTRACTING MONEY FROM NEEDS...")
#         sub_money = float(
#             input("How much do you want to subtract from NEEDS: "))
#         # stripping because for some reason if there is space in the reason, it will not do the math
#         sub_reason = input(
#             "What is the reason to subtract money: ").upper().replace(" ", "")

#         # makes sure the amount becomes negative
#         sub_money = -sub_money

#         # appends to file
#         file_opener = open("records.txt", "a")
#         file_opener.write('%-15s %15s %15s %15s\n' %
#                           (sub_reason, sub_money, 0, 0))
#         file_opener.close()

#         # print out to make sure it is correct
#         print("Output now after subtracting from NEEDS")
#         with open("records.txt", 'r') as text:
#             for line in text:
#                 print(line, end='')
#             file_opener.close()

#     elif sub_choice == 2:
#         print("1) SUBTRACTING MONEY FROM WANTS...")
#         sub_money = float(
#             input("How much do you want to subtract from WANTS: "))
#         sub_reason = input(
#             "What is the reason to subtract money: ").upper().replace(" ", "")

#         # makes sure the amount becomes negative
#         sub_money = -sub_money

#         # appends to file
#         file_opener = open("records.txt", "a")
#         file_opener.write('%-15s %15s %15s %15s\n' %
#                           (sub_reason, 0, sub_money, 0))
#         file_opener.close()

#         # print out to make sure it is correct
#         print("Output now after subtracting from WANTS")
#         with open("records.txt", 'r') as text:
#             for line in text:
#                 print(line, end='')
#             file_opener.close()

#     elif sub_choice == 3:
#         print("1) SUBTRACTING MONEY FROM SAVINGS...")
#         sub_money = float(
#             input("How much do you want to subtract from SAVINGS: "))
#         sub_reason = input(
#             "What is the reason to subtract money: ").upper().replace(" ", "")

#         # makes sure the amount becomes negative
#         sub_money = -sub_money

#         # appends to file
#         file_opener = open("records.txt", "a")
#         file_opener.write('%-15s %15s %15s %15s\n' %
#                           (sub_reason, 0, 0, sub_money))
#         file_opener.close()

#         # print out to make sure it is correct
#         print("Output now after subtracting from SAVINGS")
#         with open("records.txt", 'r') as text:
#             for line in text:
#                 print(line, end='')
#             file_opener.close()


# # option 3 - adding to money to the file
# def add():
#     print("1) Add money to needs?")
#     print("2) Add money to wants?")
#     print("3) Add money to savings?")
#     add_choice = int(input("Which one do you want to add to(1,2 or 3):"))

#     if add_choice == 1:
#         print("1 - NEEDS SELECTED")
#         # gets how much we are going to add for needs
#         add_money = float(input("How much money do you want to add to needs:"))
#         add_reason = input(
#             "What is the reason to add money:").upper().replace(" ", "")

#         # appends to file
#         file_opener = open("records.txt", "a")
#         file_opener.write('%-15s %15s %15s %15s\n' %
#                           (add_reason, add_money, 0, 0))
#         file_opener.close()

#         # print out to make sure it is correct
#         print("Output now after adding to NEEDS")
#         with open("records.txt", 'r') as text:
#             for line in text:
#                 print(line, end='')
#             file_opener.close()

#     elif add_choice == 2:
#         print("2 - WANTS SELECTED")
#         # gets how much we are going to add for wants
#         add_money = float(input("How much money do you want to add to WANTS:"))
#         add_reason = input(
#             "What is the reason to add money:").upper().replace(" ", "")

#         # appends to file
#         file_opener = open("records.txt", "a")
#         file_opener.write('%-15s %15s %15s %15s\n' %
#                           (add_reason, 0, add_money, 0))
#         file_opener.close()

#         # print out to make sure it is correct
#         print("Output now after adding to wants")
#         with open("records.txt", 'r') as text:
#             for line in text:
#                 print(line, end='')
#             file_opener.close()

#     elif add_choice == 3:
#         print("3 - SAVINGS SELECTED")
#         # gets how much we are going to add for savings
#         add_money = float(
#             input("How much money do you want to add to SAVINGS:"))
#         add_reason = input(
#             "What is the reason to add money:").upper().replace(" ", "")

#         # appends to file
#         file_opener = open("records.txt", "a")
#         file_opener.write('%-15s %15s %15s %15s\n' %
#                           (add_reason, 0, 0, add_money))
#         file_opener.close()

#         # print out to make sure it is correct
#         print("Output now after adding to savings")
#         with open("records.txt", 'r') as text:
#             for line in text:
#                 print(line, end='')
#             file_opener.close()


# # option 4 - incoming money used for budgeting
# def income():
#     # setting how much my needs are
#     needs = 0.50

#     money = float(input("How much money are you getting in: "))

#     print("\nIncoming money = ", money)

#     # now we automate the needs subtraction to know exactly how much needs money I have
#     # making variables for each different bill
#     print("\nWe have everything, now let's calculate what we need to subtract the bills from needs.")
#     car_insurance = 160.00
#     roth = 20.00
#     music = 5.46
#     gym = 10.51
#     icloud = 1.00
#     water_n_wifi = 181.00

#     # I need to know which bills need to paid depending on which paycheck
#     print("Cycle 1 = Car Insurance, roth, music, gym, and Icloud - Enter 1.")
#     print("Cycle 2 = Water and wifi - Enter 2.")
#     needs_cycle = int(input("Which cycle of bills Am I paying for(1 or 2): "))
#     while needs_cycle < 1 or needs_cycle > 2:
#         print("Not a choice!")
#         print("Cycle 1 = Car Insurance, roth, music, gym, and Icloud - Enter 1.")
#         print("Cycle 2 = Water and wifi - Enter 2.")
#         needs_cycle = int(
#             input("Which cycle of bills Am I paying for(1 or 2): "))
#     else:
#         if needs_cycle == 1:
#             print("Cycle 1...")
#             # If the money we get is not enough to cover the needs, needs will take precedence over wants/needs
#             if money <= 377:
#                 needs_total = money - car_insurance - roth - music - gym - icloud
#                 wants = 0
#                 savings = 0
#                 print("\nYour needs money is at $ ", round(needs_total, 2))
#                 print("\nYour total spending money is: $", wants)
#                 print("\nYour total saving $", round(savings, 2))

#                 print("NOW ADDING TO FILE...")
#                 # appends to file
#                 file_opener = open("records.txt", "a")
#                 file_opener.write('%-15s %15s %15s %15s\n' % ("CYCLE1-INCOME", round(needs_total, 2), wants,
#                                                               round(savings, 2)))
#                 file_opener.close()

#                 # print out to make sure it is correct
#                 print("Output now after adding to file")
#                 with open("records.txt", 'r') as text:
#                     for line in text:
#                         print(line, end='')
#                 file_opener.close()
#             else:
#                 # cal savings
#                 # setting how much I want to be able to spend each paycheck for wants
#                 # cal needs
#                 needs_total = money * needs
#                 print("\nYour needs money is at $ ", needs_total)
#                 wants = 150
#                 savings = money - needs_total - wants
#                 needs_total = needs_total - car_insurance - roth - music - gym - icloud
#                 print("\nYour needs money is at $ ", round(needs_total, 2))
#                 print("\nYour total spending money is: $", wants)
#                 print("\nYour total saving $", round(savings, 2))

#                 print("NOW ADDING TO FILE...")
#                 # appends to file
#                 file_opener = open("records.txt", "a")
#                 file_opener.write('%-15s %15s %15s %15s\n' % ("CYCLE1-INCOME", round(needs_total, 2), wants,
#                                                               round(savings, 2)))
#                 file_opener.close()

#                 # print out to make sure it is correct
#                 print("Output now after adding to file")
#                 with open("records.txt", 'r') as text:
#                     for line in text:
#                         print(line, end='')
#                 file_opener.close()
#         elif needs_cycle == 2:
#             print("Cycle 2...")
#             if money <= 332:
#                 needs_total = money - water_n_wifi
#                 wants = 0
#                 savings = 0
#                 print("\nYour needs money is at $", round(needs_total, 2))
#                 print("\nYour total spending money is: $", wants)
#                 print("\nYour total saving $", round(savings, 2))

#                 print("NOW ADDING TO FILE...")
#                 # appends to file
#                 file_opener = open("records.txt", "a")
#                 file_opener.write('%-15s %15s %15s %15s\n' % ("CYCLE2-INCOME", round(needs_total, 2), wants,
#                                                               round(savings, 2)))
#                 file_opener.close()

#                 # print out to make sure it is correct
#                 print("Output now after adding to file")
#                 with open("records.txt", 'r') as text:
#                     for line in text:
#                         print(line, end='')
#                 file_opener.close()
#             else:
#                 # cal savings
#                 # setting how much I want to be able to spend each paycheck for wants
#                 # cal needs
#                 needs_total = money * needs
#                 print("\nYour needs money is at $ ", needs_total)
#                 wants = 150
#                 savings = money - needs_total - wants
#                 needs_total = needs_total - water_n_wifi
#                 print("\nYour needs money is at $ ", round(needs_total, 2))
#                 print("\nYour total spending money is: $", wants)
#                 print("\nYour total saving $", round(savings, 2))

#                 print("NOW ADDING TO FILE...")
#                 # appends to file
#                 file_opener = open("records.txt", "a")
#                 file_opener.write('%-15s %15s %15s %15s\n' % ("CYCLE2-INCOME", round(needs_total, 2), wants,
#                                                               round(savings, 2)))
#                 file_opener.close()

#                 # print out to make sure it is correct
#                 print("Output now after adding to file")
#                 with open("records.txt", 'r') as text:
#                     for line in text:
#                         print(line, end='')
#                 file_opener.close()


# # This is income for BOCA paychecks only!
# def boca_income():
#     money = float(input("How much money are you getting in: "))

#     print("Incoming money is:", round(money, 2))

#     needs_total = 100
#     wants_total = 100
#     saving_total = money - needs_total - wants_total

#     # now add to file
#     print("NOW ADDING TO FILE...")
#     file_opener = open("records.txt", "a")
#     file_opener.write('%-15s %15s %15s %15s\n' % ("BOCA-INCOME", round(needs_total, 2), round(wants_total, 2),
#                                                   round(saving_total, 2)))
#     file_opener.close()

#     # printing out to make sure it is correct with no errors
#     print("Output after adding to file")
#     with open("records.txt", 'r') as text:
#         for line in text:
#             print(line, end='')
#     file_opener.close()


# # this totals all the columns to make things easier
# def total():
#     # Appends a line to separate the total from the amount so far
#     # file_opener = open("records.txt", "a")
#     # file_opener.write("--------------------------------------------------------------------------")
#     # file_opener.close()

#     # opening file just to make sure I can see the line
#     with open("records.txt", "r") as text:
#         for line in text:
#             print(line, end='')

#     with open('records.txt', 'r') as numbers_file:
#         total_needs = 0
#         total_wants = 0
#         total_savings = 0
#         for line in numbers_file:
#             try:
#                 total_needs += float(line.split()[1])
#                 total_wants += float(line.split()[2])
#                 total_savings += float(line.split()[3])
#             except ValueError:
#                 pass
#     print("-------------------------------------------------------------------")
#     print('%-15s %15s %15s %15s' % ("Total:", round(total_needs, 2),
#           round(total_wants, 2), round(total_savings, 2)))


# action = "Y"
# while action == "Y":
#     print("\n1) Display current amount of money.")
#     print("\n2) Subtracting money.")
#     print("\n3) Adding money.")
#     print("\n4) Incoming money that needs to be distributed.")
#     print("\n5) BOCA INCOME ONLY.")
#     user = int(input("\nMake a selection: "))
#     while user < 1 or user > 5:
#         print("Not a choice, please pick a correct option!")
#         user = int(input("\nMake a selection: "))
#     else:
#         print("You made a choice of:", user)
#         if user == 1:
#             print("Displaying current amount of money.".upper())
#             display()
#         elif user == 2:
#             print("Subtracting money.".upper())
#             sub()
#         elif user == 3:
#             print("Adding money.".upper())
#             add()
#         elif user == 4:
#             print("Incoming money.".upper())
#             income()
#         elif user == 5:
#             print("BOCA INCOME.".upper())
#             boca_income()
#         else:
#             print("Error, not a choice".upper())
#     action = input("Do you want to do another action(Y/N): ").upper()
# total()
