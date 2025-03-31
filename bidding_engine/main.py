# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)
bid_record = {}
def bidding():
    user_name = input("What's your name?")
    bid = int(input("What much do you want to bid?"))
    bid_record[user_name] = bid

should_continue = True
while should_continue:
    bidding()
    more_bid = input("Is there anyone else who'd like to bid? Type yes or no")
    while more_bid.lower() not in ("yes", "no"):
        print("Invalid answer. Try again!")
        more_bid = input("Is there anyone else who'd like to bid? Type yes or no")
    if more_bid.lower() == "yes":
        print("\n" * 20)
    elif more_bid.lower() == "no":
        should_continue = False
        print("Bidding complete. And the winner is...")
        max_bid_record = 0
        winner = ''
        for key in bid_record:
            if bid_record[key] > max_bid_record:
                max_bid_record = bid_record[key]
                winner = key
        print(winner + '!')
