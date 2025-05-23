define e = Character("Eileen", color="ffcccc")

label start:

label example_characters:
    scene bg town
    default selected_character = None
    default selected_item = None
    $ inventory = PartyInventory([], 0)
    $ inventory.say_items(e)

    define door_key = InventoryItem("Door key", "Try using it in a door.")
    $ heal_potion = Consummable("Healing potion", "inv/red potion.png", 10, 5, 0)
    $ mana_potion = Consummable("Mana potion", "inv/blue potion.png", 10, 0, 5)
    $ rejuvenation_potion = Consummable("Rejuvenation potion", "inv/purple potion.png", 40, 20, 20)
    $ axe = Weapon("Battleaxe", "inv/battleaxe.png", 100, 4, "physical")
    $ chainmail = Armor("Chainmail", "inv/chainmail_jacket.png", 200, 4, 1, "chest")
    $ copper_ring = Armor("Copper ring", "inv/copper_ring.png", 30, 0, 2, "acc")
    $ gold_ring = Armor("Gold ring", "inv/gold_ring.png", 500, 0, 8, "acc")
    $ horned_helmet = Armor("Horned helmet", "inv/horned_helmet.png", 40, 3, 0, "head")
    $ iron_buckler = Armor("Buckler", "inv/iron_buckler.png", 100, 4, -1, "shield")
    $ kite_shield = Armor("Kite shield", "inv/kite_shield.png", 200, 6, -1, "shield")
    $ leather_cap = Armor("Leather helm", "inv/leather_cap.png", 30, 1, 0, "head")
    $ longsword = Weapon("Longsword", "inv/longsword.png", 200, 6, "physical")
    $ platemail = Armor("Platemail", "inv/platemail.png", 2000, 10, 2, "chest")
    $ staff = Weapon("Staff of magic missiles", "inv/magic missile staff.png", 500, 3, "magic")



    python:
        inventory.add_item(door_key)
        inventory.add_item(heal_potion)
        inventory.add_item(heal_potion)
        inventory.add_item(mana_potion)
        inventory.add_item(rejuvenation_potion)
        inventory.add_item(axe)
        inventory.add_item(chainmail)
        inventory.add_item(copper_ring)
        inventory.add_item(gold_ring)
        inventory.add_item(horned_helmet)
        inventory.add_item(iron_buckler)
        inventory.add_item(kite_shield)
        inventory.add_item(leather_cap)
        inventory.add_item(longsword)
        inventory.add_item(platemail)
        inventory.add_item(staff)
        #inventory.say_items(e)

    $ chie = Player(7, 5, 5, 3, 2, "chie", 1)
    $ yu = Player(8, 4, 3, 5, 5, "yu", 1)
    show screen characters
    e "Notice the portrait icon in the upper left of your screen"

    e "Feel free to play with it."