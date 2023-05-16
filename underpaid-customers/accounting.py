# global variable statick price of melons, can be changed when price flactuates
melon_cost = 1.00

def payment_for_melons(cost, name, num, paid):
    """ Calculating balance for bought melons

    Taking cost for malon, name of the buyer, number of melons bought and sum paid.
    """
    customer_expected = num * cost  # calculating expected paid sum
    if customer_expected != paid:   # if overpaid or underpaid
        print(f"{name} paid ${paid:.2f},",  # print name and how much paid (trancating to 2 numbers)
          f"expected ${customer_expected:.2f}"  # and how much was expected to pay (trancating to 2 numbers)
          )


# checking price
def check_input(price):
    try:
        some_price = float(price)
        return True
    except ValueError:
        return False

# function that takes log file to check for correct
def calculate_correct_payment(customer_file):
    """ Calculating correct balance for bought melons, taking log file as an argumant.
    """
    # opening file
    the_file = open(customer_file)
    for line in the_file:
        # striping tabs, spaces, newlines
        line = line.strip()
        # getting list of words, splitting by pipeline character
        words = line.split('|')
        # reading a line we should get 4 variables
        if len(words) == 4:
            # if the input is all correct
            if words[0].isdigit() and words[2].isdigit() and check_input(words[3]):
                # converting strings to correct data type for calculating balance
                count = int(words[0])
                name = words[1]
                sold = int(words[2])
                paid = float(words[3])
                # calling function for calculating balance and printing the result
                payment_for_melons(melon_cost, name=name, num=sold, paid=paid)
        # if something else was mistakenly added to the line in log file that doesn't fit pattern
        else:
            print(f"Couldn't read and calculate this line: {line}")

    the_file.close()

# calling function with our local log file to check it
calculate_correct_payment("customer-orders.txt")