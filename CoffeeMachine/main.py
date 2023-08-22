# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "capuccino": {
      "ingredients": {
             "water": 250,
             "milk": 100,
             "coffee": 24
        },
      "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

# TODO: Ask the user for his preference

milk = 'milk'
water = 'water'
coffee = 'coffee'
ingredients = 'ingredients'


def _checkresources(drink):
    if drink == 'off':
        exit(0)
    elif drink == "report":
        print(resources)
        _inputcoffeetype()
    elif drink != 'espresso':
        if resources[milk] < MENU[drink][ingredients][milk] or resources[water] < MENU[drink][ingredients][water] or resources['coffee'] < MENU[drink][ingredients]['coffee']:
            print('ingredients not sufficient')
        elif resources[coffee] < MENU[drink][ingredients][coffee] or resources[water] < MENU[drink][ingredients][water]:
            print('ingredients not sufficient')
        else:
            print('please insert coins')
            if drink != 'espresso':
                resources[milk] -= MENU[drink][ingredients][milk]
                resources[water] -= MENU[drink][ingredients][water]
                resources[coffee] -= MENU[drink][ingredients][coffee]
            else:
                resources[water] -= MENU[drink][ingredients][water]
                resources[coffee] -= MENU[drink][ingredients][coffee]
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    Amount = round(float(0.25*quarters +0.1*dimes +0.05*nickles +0.01*pennies))
    if Amount > MENU[drink]['cost']:
        print(f"Here is your change {Amount-MENU[drink]['cost']}")
        print(f"Here is your {drink}. enjoy!!!")
        _inputcoffeetype()
    elif Amount < MENU[drink]['cost']:
        print("sorry that's not enough money.Money refunded")
        _inputcoffeetype()
    else:
        print(f"Here is your {drink}. enjoy!!!")
        _inputcoffeetype()

def _inputcoffeetype():
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    _checkresources(coffee)


_inputcoffeetype()












# for key in MENU:
#         print(key, MENU[key])
# iterate through the loop and compare the values against ingredients to check if they are sufficient





