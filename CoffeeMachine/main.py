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

turn = "on"
profit = 0


# TODO:5. Process coins.
def coins(coffee_cost):
    quarters = float(input("how many quarters?: $"))
    dimes = float(input("how many dimes?: $"))
    nickles = float(input("how many nickles?: $"))
    pennies = float(input("how many pennies?: $"))
    result = (quarters * 0.25) + (dimes * 0.10) + (nickles + 0.05) + (pennies * 0.01)

    if result >= coffee_cost:
        print(f"Here is {result - coffee_cost} in change ")
        return True
    else:
        return False


# TODO:4. Check resources sufficient?.
def check(coffee_name):
    # get the water
    water = MENU[coffee_name]["ingredients"]["water"]
    # the milk value
    if "milk" in MENU[coffee_name]["ingredients"].keys():
        milk = MENU[coffee_name]["ingredients"]["milk"]
    else:
        milk = 0
    # coffee
    coffee = MENU[coffee_name]["ingredients"]["coffee"]
    # cost
    cost = MENU[coffee_name]["cost"]

    if water > resources["water"]:
        print("Sorry there is not enough water")
        return False
    elif milk > resources["milk"]:
        print("Sorry there is not enough milk")
        return False
    elif coffee > resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    else:
        money = coins(cost)
        if money:
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            print(f"Here is your {coffee_name} ☕️ Enjoy! \n")
            return cost
        else:
            print(f"Sorry that's not enough money. Money refunded. 🤑")


# TODO:1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):".
while turn == "on":
    order = input("What Would You Like (espresso $1.5 /latte $2.5 /cappuccino $3.0): ")

    # TODO:2. Turn off the Coffee Machine by entering “off”to the prompt.
    if order == "off":
        turn = "off"

    # TODO:3. Print report.
    elif order == "report":
        print("The current resource values")
        for key in resources:
            if key == "coffee":
                print(f"{key}: {resources[key]} g")
            else:
                print(f"{key}: {resources[key]} ml")
        print(f"Money: ${profit}")

    # TODO:4. Check resources sufficient?.
    elif order == "espresso":
        check_cost = check("espresso")
        if not check_cost:
            pass
        else:
            profit += check_cost
    elif order == "latte":
        check_cost = check("latte")
        if not check_cost:
            pass
        else:
            profit += check_cost

    elif order == "cappuccino":
        check_cost = check("cappuccino")
        if not check_cost:
            pass
        else:
            profit += check_cost
    else:
        print("Please write the coffee name correctly")
