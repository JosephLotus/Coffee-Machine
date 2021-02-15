name ='''
                          ad88    ad88
                        d8"     d8"
                        88      88
 ,adPPYba,  ,adPPYba, MM88MMM MM88MMM ,adPPYba,  ,adPPYba,
a8"     "" a8"     "8a  88      88   a8P_____88 a8P_____88
8b         8b       d8  88      88   8PP""""""" 8PP"""""""
"8a,   ,aa "8a,   ,a8"  88      88   "8b,   ,aa "8b,   ,aa
 `"Ybbd8"'  `"YbbdP"'   88      88    `"Ybbd8"'  `"Ybbd8"' 
 
 
                        (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
  jgs \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""` 
 
'''

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


def check_resources(drink):
    """This function checks the current resources to ensure there are enough for chosen drink"""
    water_needed = MENU[drink]['ingredients']['water']
    milk_needed = MENU[drink]['ingredients']['milk']
    coffee_needed = MENU[drink]['ingredients']['coffee']
    return water_needed, milk_needed, coffee_needed


def espresso_resources(drink):
    """This function checks the current resources to ensure there are enough for chosen drink"""
    water_needed = MENU[drink]['ingredients']['water']
    coffee_needed = MENU[drink]['ingredients']['coffee']
    return water_needed, coffee_needed


def report():
    """This function prints the current values of each resource"""
    print("Current resources...")
    print(f"    Water:   {resources['water']}ml")
    print(f"    Milk:    {resources['milk']}ml")
    print(f"    Coffee:  {resources['coffee']}g")
    print(f"    Money:   ${money}")


def calculate_coins(quarters, dimes, nickles, pennies):
    """This function calculates the total amount of money inserted"""
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


machine_on = True
choice_made = False
money = 0

print(name)

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        report()
    else:
        if choice == 'espresso':
            water, coffee = espresso_resources(choice)
            if water > resources['water']:
                print("Sorry, there is not enough water.")
            elif coffee > resources['coffee']:
                print("Sorry, there is not enough coffee.")
            else:
                choice_made = True
        else:
            water, milk, coffee = check_resources(choice)
            if water > resources['water']:
                print("Sorry, there is not enough water.")
            elif milk > resources['milk']:
                print("Sorry, there is not enough milk.")
            elif coffee > resources['coffee']:
                print("Sorry, there is not enough coffee.")
            else:
                choice_made = True
    if choice_made:
        # This section takes the change
        print("Please insert coins.")
        quarters_inserted = int(input("How many quarters?: "))
        dimes_inserted = int(input("How many dimes?: "))
        nickles_inserted = int(input("How many nickles?: "))
        pennies_inserted = int(input("How many pennies?: "))

        # This section checks to make sure that enough money was inserted for the given selection
        money_needed = MENU[choice]['cost']
        money_inserted = calculate_coins(quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted)

        if money_inserted < money_needed:
            print("Sorry, that isn't enough money. Money refunded.")
        else:
            money += money_needed
            if money_inserted > money_needed:
                change = round(money_inserted - money_needed, 2)
                print(f"Here is your ${change} dollars in change.")
            print(f"Here is your {choice}. Enjoy!")
            resources['water'] -= water
            resources['coffee'] -= coffee
            if choice != 'espresso':
                resources['milk'] -= milk
            choice_made = False

print("Entering sleep mode... Goodnight.")
