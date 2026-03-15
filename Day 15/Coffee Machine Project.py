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
money = 0
total = 0
status_machine = True
def format_resources():
  resource_water = resources["water"]
  resource_milk  = resources["milk"]
  resources_coffee = resources["coffee"]
  return f"Water: {resource_water}ml\nMilk: {resource_milk}ml\nCoffee: {resources_coffee}g\nMoney: ${total}"
#TODO 4: Check resouces sufficient?
def resources_insufficient(drink):
  for item in MENU[drink]["ingredients"]:
    if resources[item] < MENU[drink]["ingredients"][item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True
  
def update_resource(drink):
  for item in MENU[drink]["ingredients"]:
    resources[item] -= MENU[drink]["ingredients"][item]
  
def process_coins():
  print("Please insert coins.")
  quarters = int(input("How many quarters?"))
  dimes = int(input("How many dimes?"))
  nickles = int(input("How many nickles?"))
  pennies = int(input("How many pennies?"))
  total_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
  return total_money

while status_machine:
  #TODO 1: check the user's input to decice what to do next
  user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
  #TODO 2: Turn of the coffee machine by entering "off" to the prompt.
  if user_input == "off":
    status_machine  = False
  #TODO 3: Print report.
  elif user_input == "report":
    print(format_resources())
  #TODO 6: Check transaction successful?
  elif user_input in ["espresso","latte","cappuccino"]:
    if resources_insufficient(user_input):
      #TODO 5: Process coins.
      buyer_money = process_coins()
      drink_cost = MENU[user_input]["cost"]
      #TODO 7: Make coffee.
      if buyer_money >= drink_cost:
        change = round(buyer_money - drink_cost,2)
        if change > 0:
          print(f"Here is ${change} in change.")
        update_resource(user_input)
        total += drink_cost
        print(f"Here is your {user_input} ☕ Enjoy!")
      else:
        print("Sorry that's not enough money. Money refunded.")
  else:
    print("Invalid input. Please try again.")


