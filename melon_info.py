"""Print out all the melons in our inventory."""
import json

with open('melons.json') as f:
  melon_data = json.load(f)

for i in range(len(melon_data["melon data"])):
    """
        "name": "Honeydew",
        "price": 0.99,
        "seeds": false,
        "flesh color": "green",
        "rind color": "brown",
        "average weight": 1.0,
        "zip code where grown": 95125
    """
    for key in melon_data["melon data"][i]:
        if key == 'name':
            print(melon_data["melon data"][i][key].upper())
        else:   
            print(f"\t{key}: {melon_data['melon data'][i][key]}")
    print("\n")
