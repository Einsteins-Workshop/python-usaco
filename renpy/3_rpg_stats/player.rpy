init python:
    class Player:
        def __init__(self, hp, mp,img_prefix, level = 1):
            self.img_icon = f"{img_prefix} icon idle.png"
            self.hp = 1
            self.mp = 1
            self.max_hp = hp
            self.max_mp = mp
            self.level = level
            self.weapon = None
            #self.armor = {"head": None, "chest": None, "acc": None, "shield": None}

        def add_hp(self, amount):
            print("This has not yet been implemented")

        def add_mp(self, amount):
            print("This has not yet been implemented")

        def equip_weapon(self, weapon, inventory):
            if self.weapon != None:
                self.unequip_weapon(inventory)
            self.weapon = weapon
            inventory.remove_item(weapon)

        def unequip_weapon(self, inventory):
            inventory.add_item(self.weapon)
            self.weapon = None

        def equip_armor(self, armor, slot, inventory):
            print("This has not yet been implemented")

        def unequip_armor(self, slot, inventory):
            print("This has not yet been implemented")
