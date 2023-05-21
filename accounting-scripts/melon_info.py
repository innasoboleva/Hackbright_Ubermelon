"""Print out all the melons in our inventory."""


from melons import melons 


def print_melon_info(dict):
     """Print each melon with corresponding attribute information.
     
        Function takes dictionary as an argument with all melon's data.
     """

     for melon in dict:
        print(melon.upper())    # getting melon's name
        for key in dict[melon].keys():      # getting all data (keys) for each melon
             print(f"{key}: {dict[melon][key]}")
        print()

print_melon_info(melons)