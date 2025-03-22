from data import flavours

# Function check resourses
resourses = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
    }
money_machine = 0
error = False

def check_resourses(resourses_left):
    ingredients = flavours[order]["ingredients"]
    new_resourses = {}

    for ingredient in ingredients.keys():
        if resourses_left[ingredient] >= ingredients[ingredient]:
            new_resourses[ingredient] = resourses_left[ingredient] - ingredients[ingredient]
        else:
            print(f"Sorry! There is not enough {ingredient}")
            global error
            error = True
    return new_resourses


def check_coins():
    error = True
    change_order = 0
    while error:
        quarters = int(input('How many quarters?: '))
        dimes = int(input('How many dimes?: '))
        nickles = int(input('How many dimes?: '))
        pennies = int(input('How many pennies?: '))

        inserted = (0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies)
        cost = flavours[order]["cost"]
        change_order = inserted - cost

        if cost > inserted:
            print("Not enough money. Try again.")
            error = True
            continue
        global money_machine
        money_machine += cost
        error = False

    return change_order


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print(f'Water: {resourses["water"]}ml\nMilk: {resourses["milk"]}ml\nCoffee: {resourses["coffee"]}g\nMoney: ${money_machine}')
    elif order in ['espresso', 'latte', 'cappuccino']:
        resourses = check_resourses(resourses)
        if error:
            break
        else:
            print('Please, insert coins.')
            change = check_coins()
            print(f"Here is ${change:.2f} in change")
            print(f"Here is you latte ☕ Enjoy!")

