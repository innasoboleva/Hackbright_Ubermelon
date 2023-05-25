"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

# Create file object to read the file
f = open('sales-report.txt')

for line in f:
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