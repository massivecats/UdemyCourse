# numbers = "5,14,8,7,31,6"
# print(numbers)
# print(numbers.split(","))
#
# user_input = input("Yo. Enter your numbers, seperated by commas: ")
# user_numbers = user_input.split(",")
# user_numbers_int = []
#
# for number in user_numbers:
#     user_numbers_int.append(int(number))
#
# print(user_numbers)
# print(user_numbers_int)
#
# print([int(numbers) for numbers in user_numbers])

# -- lection 27: sets --
# lottery_values = {3, 5, 16, 2} # sets are defined with {}, elements are unique
# user_values = {3, 5, 90, 9}
# print(lottery_values)
# print(user_values)
#
# wowmanyvalues = lottery_values.intersection(user_values) # .intersection returns only the elements that are present in BOTH sets
# print(wowmanyvalues)

# -- lection 28: lottery app!
# user can pick 6 numbers (between 1 and 20), lottery calculates 6 random numbers, match users numbers to lottery numbers

import random

def menu():
    player_numbers = get_player_numbers() # ask player for numbers
    lottery_numbers = create_lottery_numbers() # calculate lottery numbers
    winnings = player_numbers.intersection(lottery_numbers) # print out winnings

    if len(winnings) == 0:
        print("Unfortunately you failed to get any numbers. Sorry!")
    else:
        print("Thank you for playing. You got the numbers {} correct and won {}€. Congrats!".format(winnings, 100 ** len(winnings)))

def get_player_numbers():
    player_numbers_csv = input("Enter your 6 numbers, between 1 and 20, seperated by commas: ")
    # create set of integers from user_numbers_csv
    player_numbers_list = player_numbers_csv.split(",") # [1,2,3,...]
    # user_numbers_set = set()
    # for number in user_numbers_list:
    #     user_numbers_set.add(int(number))
    player_numbers_set = {int(number) for number in player_numbers_list} # shorter
    return player_numbers_set

def create_lottery_numbers():
    lottery_numbers_set = set()
    # for numbers in range(6):
    #     lottery_numbers.add(random.randint(1,20)) # runs 6 times, every times, but can create 1 value multiple times, which can not be added to a ser

    while len(lottery_numbers_set) < 6:
        lottery_numbers_set.add(random.randint(1,20))
    return lottery_numbers_set

menu()












# :)
