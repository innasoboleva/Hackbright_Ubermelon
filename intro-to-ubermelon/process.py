log_file = open("um-server-01.txt")
# reading file named um-server-01.txt

def generate_sales_reports(log_file):
# for each line in log file
    for line in log_file:
# striping spaces, tabs, newlines
        line = line.rstrip()
# reading first 3 characters on a line
        day = line[0:3]
# if it is equal to desired day, then display =
        if day == "Mon":
            print(line)


generate_sales_reports(log_file)
