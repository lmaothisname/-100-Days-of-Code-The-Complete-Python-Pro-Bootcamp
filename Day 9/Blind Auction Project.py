# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
ask = "yes"
people_auction = {
        "player" : [],
        "money" : []
    }
while ask != "no":
    name_auction = input("What's your name?: ")
    bid_auction = int(input("What's your bid?: $"))
    people_auction["player"].append(name_auction)
    people_auction["money"].append(bid_auction)
    temp = people_auction["money"][0]
    ask = input("Are there any other bidders? Type 'yes' or 'no.\n")
    if ask == "yes":
        print("\n" * 20)
    if ask == "no":
        for key in people_auction["money"]:
            if key > temp:
                temp = key
        get_index = people_auction["money"].index(temp)
        print(f"The winner is {people_auction['player'][get_index]} with a bid of ${people_auction['money'][get_index]}")


