"""Print out all the melons in our inventory."""


from melons import melons 


def print_melon_info(dict):
     """Print each melon with corresponding attribute information."""

     for melon in dict:
        print(melon.upper())
        for key in dict[melon].keys():
             print(f"{key}: {dict[melon][key]}")
        print()

print_melon_info(melons)