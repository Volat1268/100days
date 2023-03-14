from art import art_text, emoji
from data import MENU, resources


# ------------------------functions------------------------------------------


def user_choice(user_choice):
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        return make_coffee()
    if user_choice == "report":
        return report()
    if user_choice == "of":
        return take_off()
    else:
        pass


def make_coffee():
    pass


def report():
    pass


def take_off():
    pass


# ----------------------- variables-----------------------------------------------
water_left = resources["water"]
milk_lef = resources["milk"]
coffee_lef = resources["coffee"]
espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]
espresso_water_use = MENU["espresso"]["ingredients"]["water"]
espresso_coffee_use = MENU["espresso"]["ingredients"]["coffee"]
latte_water_use = MENU["latte"]["ingredients"]["water"]
latte_coffee_use = MENU["latte"]["ingredients"]["coffee"]
cappuccino_water_use = MENU["cappuccino"]["ingredients"]["water"]
cappuchino_coffee_use = MENU["cappuccino"]["ingredients"]["coffee"]

# ----------------------- programme-------------------------------------



# print(art_text)
# user_choice = input("What would you like? (espresso (cost: 1.5)/latte (cost: 2.5)"
#                     "/cappuccino (cost: 3.0))").lower()
# print("Please insert coins.")
# print("How many quarters?")
# print("How many dims?")
# print("How many nickles?")
# print("How many pennies?")
# print("Sorry, that's not enough money. Money refunded.")
# print(f"Hire is {} in change.")
# print(f"Hire is your {} {emoji}. Enjoy!")


mat_choice(2)
