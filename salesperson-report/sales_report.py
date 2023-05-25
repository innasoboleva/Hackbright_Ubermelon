"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

sales = {}

# Create file object to read the file
f = open('sales-report.txt')

for line in f:  # for each line in the file object
    line = line.rstrip()    # remove extra character to the right
    entries = line.split('|')   # splitting words by pipeline and creating a list "entries" with strings 
    salesperson = entries[0]    # assigning first string to salesperson variable
    melons = int(entries[2])    # assigning third string to melons variable and converting it to integer

    if salesperson in salespeople:  # if that person exists in array
        position = salespeople.index(salesperson)   # gettin index of that person
        melons_sold[position] += melons     # incrementing melons at that position in melons_sold array
        
    else:
        salespeople.append(salesperson) # if person is not present in salespeople array, adding him
        melons_sold.append(melons)  # appending to melons_sold list melons


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # printing the result

# IMPOVEMENTS: To make it faster and easier to read, dictionary 
# should be used instead of making connections between two arrays by their index position.

f.close()
# Create file object to read the file
f = open('sales-report.txt')

for line in f:  # for each line in the file object
    line = line.rstrip()    # remove extra character to the right
    entries = line.split('|')   # splitting words by pipeline and creating a list "entries" with strings 
    if entries[0] and entries[2]:   # if both values are True and not empty strings
        if entries[2].isdigit():    # if ammaunt of melons is a valid input, that consists of digit
            if entries[0] in sales:     # if that person already exists in dictionary "sales"
                sales[entries[0]] += int(entries[2])    # add sold melons to that entry
            else:
                sales[entries[0]] = int(entries[2])     # if not in dict, create new key,value pair

for name,melons in sales.items():
    print(f'--- {name} sold {melons} melons') # printing the result
        