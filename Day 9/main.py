from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

bid_collection = {}
# other_bids = input("Are there more people looking to bid? 'Y' or 'N'")
bid_start = True


def winner(bid_collection):
    highest_bid = 0
    for bid in bid_collection:

        if bid_collection[bid] > highest_bid:
            winner_name = bid
            highest_bid = bid_collection[bid]
    clear()
    print(f"The winner is {winner_name} with a bid of ${highest_bid}")
    

while bid_start:
    other_bids = input("Are there more people looking to bid? Type 'Y' or 'N'\n").lower()
    if other_bids == 'y':
        clear()
        users_name = input("What is your name? ")
        users_bid = int(input("What is your bid price? "))
        bid_collection[users_name] = users_bid
    else:
        winner(bid_collection)
        bid_start = False