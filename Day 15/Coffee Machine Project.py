MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def format_resources(rp):
    resources_milk = resources["milk"]
    resources_water = resources["water"]
    resources_coffee = resources["coffee"]
    return f"Water: {resources_water}ml\nMilk: {resources_milk}ml\nCoffee: {resources_coffee}g"
total = 0
def buyer_purchaser(quarters,dimes,nickles,pennies):
    sum = 0.25 * quarters + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return sum
machine_on_off = True
def resources_insufficient_espresso():
    if resources["water"] - MENU["espresso"]["ingredients"]["water"] < MENU["espresso"]["ingredients"]["water"]:
        return "Sorry there is not enough water."
    else:
        return "Sorry there is not enough coffee."
def resources_insufficient_latte():
    if resources["water"] - MENU["latte"]["ingredients"]["water"] < MENU["latte"]["ingredients"]["water"]:
        return "Sorry there is not enough water."
    elif resources["coffee"] - MENU["latte"]["ingredients"]["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee."
    else:
        return "Sorry there is not enough milk."
def resources_insufficient_cappuccino():
    if resources["water"] - MENU["cappuccino"]["ingredients"]["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        return "Sorry there is not enough water."
    elif resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
        return "Sorry there is not enough coffee."
    else:
        return "Sorry there is not enough milk."
# ToDo 1: create a promt "What would you like"
while machine_on_off:
    ask_user = input("What would you like? (espresso/latte/cappuccino): ")
    if ask_user == "report":
        print(format_resources(resources))
    elif ask_user == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            print("please insert a coin ?")
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            buyer_quarters = int(input("How many quarters?: "))
            buyer_dimes = int(input("How many dimes?: "))
            buyer_nickles = int(input("How many nickles?: "))
            buyer_pennies = int(input("How many pennies?: "))
            total = buyer_purchaser(buyer_quarters,buyer_dimes,buyer_nickles,buyer_pennies)
            if total > MENU["espresso"]["cost"]:
                refund_money = total - MENU["espresso"]["cost"]
                print(f"Here is ${refund_money} in change.")
                print("Here is your espresso ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            resources_insufficient_espresso()
    elif ask_user == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >=  MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            print("please insert a coin ?")
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            buyer_quarters = int(input("How many quarters?: "))
            buyer_dimes = int(input("How many dimes?: "))
            buyer_nickles = int(input("How many nickles?: "))
            buyer_pennies = int(input("How many pennies?: "))
            total = buyer_purchaser(buyer_quarters,buyer_dimes,buyer_nickles,buyer_pennies)
            if total > MENU["latte"]["cost"]:
                refund_money = total - MENU["latte"]["cost"]
                print(f"Here is ${refund_money} in change.")
                print("Here is your latte ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            resources_insufficient_latte()
    elif ask_user == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >=  MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            print("please insert a coin ?")
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            buyer_quarters = int(input("How many quarters?: "))
            buyer_dimes = int(input("How many dimes?: "))
            buyer_nickles = int(input("How many nickles?: "))
            buyer_pennies = int(input("How many pennies?: "))
            total = buyer_purchaser(buyer_quarters,buyer_dimes,buyer_nickles,buyer_pennies)
            if total > MENU["cappuccino"]["cost"]:
                refund_money = total - MENU["cappuccino"]["cost"]
                print(f"Here is ${refund_money} in change.")
                print("Here is your cappuccino ☕ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(resources_insufficient_cappuccino())
    else:
        machine_on_off = False