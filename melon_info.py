"""Print out all the melons in our inventory."""
import json

# Stored my nested dict in a .json file
with open('melons.json') as f:
  melon_data = json.load(f)

for melon_name in melon_data:
    """ Use a nested dict to print all melon data.

    {
        "Cantaloupe": {
            "price": 2.00,
            "seeds": true,
            "flesh color": "orange",
            "rind color": "brown",
            "average weight": 2.2,
            "zip code where grown": 12554
        }, ...
    }
    """
    print(melon_name.upper())
    for attribute_key in melon_data[melon_name]:
        print(f"\t{attribute_key}: {melon_data[melon_name][attribute_key]}")
    print("\n")
