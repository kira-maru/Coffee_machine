from dictionary import MENU, resources, coins
from functions import resources_check, client_payment, processing_order, resources_replenishment

def machine_working():

    can_brew = True

    while can_brew:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "report":
            print(f"Resources: {resources}")
        else:
            # Check if the ingredients are sufficient
            report = resources_check(order, MENU, resources)
            if not report:
                maintanence = input("Maintanence needed. Do you want to proceed? (y/n): ")
                if maintanence == "n":
                    can_brew = False
                    break
                else:
                    resources_replenishment(resources)
                    continue


            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            nickles = int(input("How many nickles?: "))
            dimes = int(input("How many dimes?: "))
            pennies = int(input("How many pennies?: "))
            amount_paid = client_payment(quarters, nickles, dimes, pennies, coins)

            order_result = processing_order(amount_paid, order, MENU)
            if order_result == False:
                can_brew = False
                # machine_working()
                break
            else:
                print(order_result)





machine_working()


























