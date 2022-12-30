from art import MENU, resources


def coffee(s, user_money):
    """checks for the money inserted by the user"""
    real_money = MENU[s]["cost"]
    print(real_money)
    print(user_money)
    if user_money > real_money:
        change = user_money - real_money
        print("Here is your change: $", change)
        print("Here is your "+choice + "☕ Enjoy😊")
        return real_money
    elif user_money < real_money:
        print("Not enough coins. Money refunded")


def check_resources(ch):
    """Checks if the ingredients are sufficient or not for the coffee"""
    ingo = MENU[ch]["ingredients"]
    if resources["water"] < ingo["water"]:
        print("Not enough water.")
        return True
    elif ch != "espresso" and resources["milk"] < ingo["milk"]:
        print("Not enough milk")
        return True
    elif resources["coffee"] < ingo["coffee"]:
        print("Not enough coffee")
        return True
    else:
        return False


def report(money_in):
    """Gives the report for ingredients"""
    print("Water: ", resources["water"])
    print("Milk: ", resources["milk"])
    print("Coffee: ", resources["coffee"])
    print(f"Money: {money_in}")


def ingredient_record(c):
    """keeps track of the quantity of ingredients"""
    resources["water"] -= MENU[c]["ingredients"]["water"]
    resources["coffee"] -= MENU[c]["ingredients"]["coffee"]
    if c != "espresso":
        resources["milk"] -= MENU[c]["ingredients"]["milk"]


def money(q, d, n, p):
    """Takes input and calculates the total money in dollars"""
    total_money = q*0.25 + d*0.10 + n*0.05 + p*0.01
    return total_money


op = True
m = 0
while op:
    # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: Ask the user to enter the coins
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print("Please insert coins.")
        quarter = int(input("how many quarters?"))
        dimes = int(input("how many dimes?"))
        nickles = int(input("how many nickles?"))
        pennies = int(input("how many pennies?"))

        Total_money = money(quarter, dimes, nickles, pennies)
        m += coffee(choice, Total_money)
        ingredient_record(choice)
    # TODO: Give report if inputted
    elif choice == "report":
        report(m)
        # TODO: Turn off the Coffee Machine by entering “off” to the prompt.
    elif choice == "off":
        op = False
    # TODO: Check resources sufficient?
    elif check_resources(choice):
        print("Not enough resources.")
        op = False






