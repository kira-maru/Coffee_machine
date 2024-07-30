def resources_check(order, MENU, resources):
    if order in MENU:
        for ingredient, amount in MENU[order]["ingredients"].items():
            if amount > resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
            else:
                resources[ingredient] -= amount
        return resources

    else:
        return resources


def client_payment(coin1, coin2, coin3, coin4, coins):
    coin1 = coin1 * coins["quarters"]
    coin2 = coin2 * coins["nickles"]
    coin3 = coin3 * coins["dimes"]
    coin4 = coin4 * coins["pennies"]
    sum = coin1 + coin2 + coin3 + coin4

    return sum


def processing_order(amount_paid, order, MENU):
    if amount_paid == MENU[order]["cost"]:
        return f"Here is your {order}. Enjoy!"
    elif amount_paid > MENU[order]["cost"]:
        change = amount_paid - MENU[order]["cost"]
        return f"Here is ${round(change, 2)} in change.\nEnjoy your {order}!"
    elif amount_paid < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False

def resources_replenishment(resources):
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


