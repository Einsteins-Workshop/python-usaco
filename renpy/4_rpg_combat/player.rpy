init python:
    class Player:
        def __init__(self, hp, mp, atk, defense, mdef, img_prefix, level = 1):
            self.img_icon = f"{img_prefix} icon idle.png"
            self.hp = 1
            self.mp = 1
            self.max_hp = hp
            self.max_mp = mp
            self.atk = atk
            self.defense = defense
            self.mdef = mdef
            self.level = level
            self.weapon = None
            self.armor = {"head": None, "chest": None, "acc": None, "shield": None}

        def add_hp(self, amount):
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

        def add_mp(self, amount):
            self.mp += amount
            if self.mp > self.max_mp:
                self.mp = self.max_mp

        def equip_weapon(self, weapon, inventory):
            if self.weapon != None:
                self.unequip_weapon(inventory)
            self.weapon = weapon
            self.atk += weapon.atk
            inventory.remove_item(weapon)

        def unequip_weapon(self, inventory):
            self.atk -= self.weapon.atk
            inventory.add_item(self.weapon)
            self.weapon = None

        def equip_armor(self, armor, slot, inventory):
            if self.armor[slot] != None:
                self.unequip_armor(slot, inventory)
            self.armor[slot] = armor
            self.defense += armor.defense
            self.mdef += armor.mdef
            inventory.remove_item(armor)

        def unequip_armor(self, slot, inventory):
            if self.armor[slot] != None:
                self.defense -= self.armor[slot].defense
                self.mdef -= self.armor[slot].mdef
                inventory.add_item(self.armor[slot])
                self.armor[slot] = None
