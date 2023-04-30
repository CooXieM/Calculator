import pandas
from datetime import date


# Introduction -
def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = '{} {} {}'.format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)
    return ""


# Functions ------------

# Checkers user has answered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either Yes or No: \n")


# Checks users response is not blank -
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print(f"{error}. \nPlease try again\n")
            continue

        return response


# Number checker - first
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Number checker - second
def cost_checker(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer")


# Currency
def currency(x):
    return "${:.2f}".format(x)


# data frane abd sub total
def get_expenses(var_fixed):
    # Dictionary -
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Main Routine ---

    # Date time at the start -
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    heading = "The current date is {}/{}/{}".format(day, month, year)
    print(heading)

    amount_produced = 0

    # Print Welcoming Heading
    statement_generator("Welcome to the Fund Raiser Calculator", "=")

    # Ask if instructions are needed -
    want_instructions = yes_no("\n Would you like to see the Instructions to this program?")
    if want_instructions == 'yes':
        print("Instructions goes here")
    print()

    # amount_produced = num_check("How many items will you be producing? ")

    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # Get name, Quantity and item
        item_name = not_blank("Item name (or type 'xxx' to quit): ", "This cannot be black. ")
        if item_name.lower() == "xxx":
            break   
        quantity = num_check("Quantity: ", "This must be a whole number, More than 0",
                             int)
        price = num_check("Price for an item? $",
                          "Price must be a number <More Than 0>",
                          float)

        # add item, quantity and price list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of components
    expense_frame['Cost'] = expense_frame['Quantity'] \
                            * expense_frame['Price']

    # Find subtotal
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

        return [expense_frame, sub_total]


# *** Main Routine ***
product_name = not_blank("Product name: ", "The Product name cannot be empty")

fixed_expenses = get_expenses("Fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[0]

# *** Printing Area ***
print()
print(fixed_frame[['Cost']])
print()

print("Fixed Cost: ${:.2f}".format(fixed_sub))
