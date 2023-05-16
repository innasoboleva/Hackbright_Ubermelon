# creating a function
def print_report_for_day(day, file):
    print("Day", day)
# creating object from a file to be able to access it
    the_file = open(file)
# for each line
    for line in the_file:
    # stripping spaces, tabs to the right
        line = line.rstrip()
    # making list of strings, splitting it by | character
        words = line.split('|')
    # assigning variable for melon, count and amount
        melon = words[0]
        count = words[1]
        amount = words[2]
    # printing the result
        print(f"Delivered {count} {melon}s for total of ${amount}")
    # closing opened file, so not keeping it in memory open
    the_file.close()


print_report_for_day(1, "um-deliveries-day-1.txt")
print_report_for_day(2, "um-deliveries-day-2.txt")
print_report_for_day(3, "um-deliveries-day-3.txt")
