# Dictionaries are a way of creating a collection with named keys instead of the numerical indexes
# of lists.  This is great for lookup tables.

# You can create a dictionary using {}:

orc_1 = {
    "hit_points": 10,
    "attack": 3,
    "defense": 1
}

print("Stats for orc 1:")
print(orc_1)

# You can access and change values similar to how you use lists, but using the named keys instead

print("Orc hit points:")
print(orc_1["hit_points"])

print("The orc takes 3 damage.")
orc_1["hit_points"] = orc_1["hit_points"] - 3

# Set new attributes, speed, x_position, y_position
orc_1["speed"] = 3
position = {
    "x_position": 10,
    "y_position": 12
}
orc_1.update(position)
print("Adding new attributes")
print(orc_1)

# Deleted items can be used with del keyword
del orc_1["x_position"]
del orc_1["y_position"]
print("Removing position from orc")
print(orc_1)

# You can loop through a dictionary similar to a list
print("Orc attributes:")
for key in orc_1:
    print(key)

print("All orc values:")
for value in orc_1.values():
    print(value)

print("Here are the orc's stats:")
for key, value in orc_1.items():
    print(key, value)

# You can also copy dictionaries, which copies the values of the original dictionary, and each can be changed
# indepedently.
orc_2 = orc_1.copy()
orc_3 = dict(orc_1)
orc_2['hit_points'] = 10
print("Orc 1 and Orc 2:")
print(orc_1)
print(orc_2)

# You can also have a nested dictionary

players = {
    "Arwen" : {
        "hit_points": 10,
        "attack": 3,
        "defense": 2
    },
    "Baldur": {
        "hit_points": 12,
        "attack": 2,
        "defense": 3
    }
}