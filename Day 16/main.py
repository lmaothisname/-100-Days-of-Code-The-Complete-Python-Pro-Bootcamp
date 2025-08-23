from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item = Menu()
status_machine = True
while status_machine:
    options = menu_item.get_items()
    ask_user = input(f"What would you like? ({options}): ")
    if ask_user == "report":
        coffee_maker.report()
        money_machine.report()
    elif ask_user == "off":
        status_machine = False
    else:
        drink = menu_item.find_drink(ask_user)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)