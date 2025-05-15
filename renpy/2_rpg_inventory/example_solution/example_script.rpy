define e = Character("Eileen", color="ffcccc")

label start:

label example_inventory:
    scene bg town
    show eileen happy
    $ inventory = Inventory(e, [], 0)
    $ inventory.say_items()

    define door_key = InventoryItem("Door key", "Try using it in a door.")
    $ chest_key = InventoryItem("Chest key", "Try using it in a chest.")
    $ stack_of_money = InventoryItem("Stack of money", "Phat and juicy.")
    $ potion = ConsummableItem("Rejuvenation potion", 10, 10)
    $ gem = LootItem("Quartz", 5)

    e "I'm going to pick up these keys."
    e "Now lets see what I'm carrying."
    python:
        inventory.add_item(door_key)
        inventory.add_item(chest_key)
        inventory.say_items()
    e "Now I'm going to use up a key and get the loot."
    python:
        inventory.remove_item(chest_key)
        inventory.add_item(stack_of_money)
        inventory.add_item(potion)
        inventory.add_item(gem)

    e "Now let's display the inventory option"
    show screen hud
    e "Notice the backpack icon in the upper left of your screen"

    e "Feel free to play with it."
