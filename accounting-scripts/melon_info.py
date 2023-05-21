"""Print out all the melons in our inventory."""


from melons import melons 


def print_melon_info(dict):
     """Print each melon with corresponding attribute information."""

     for melon in dict:
         print(melon)
         for key, value in enumerate(melon):
             print(f"{key}: {value}")


print_melon_info(melons)