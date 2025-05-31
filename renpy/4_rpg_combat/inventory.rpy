init python:
    class StatItem():
        def __init__(self, name, img, value):
            self.name = name
            self.img = img
            self.value = value
        def __call__(self):
            return self.to_string()

        def to_string(self):
            return f"{self.name} ({self.value})"

    class PartyInventory():
        def __init__(self, items, item_count):
            self.items = items
            self.item_count = item_count
            self.displayable_items = list(filter(lambda x: isinstance(x, StatItem), items))

        def add_item(self, item):
            self.items.append(item)
            self.item_count += 1
            if isinstance(item, StatItem):
                self.displayable_items.append(item)

        def remove_item(self, item):
            self.items.remove(item)
            self.item_count -= 1
            if isinstance(item, StatItem):
                self.displayable_items.remove(item)

        def say_items(self, character):
            if (len(self.items)) < 1:
                say(character, "I'm not carrying anything.")
            else:
                say(character, "I'm currently carrying:")
                for item in self.items:
                    say(character, item())

    class Consummable(StatItem):
        def __init__(self, name, img, value, hp_gain, mp_gain):
            StatItem.__init__(self, name, img, value)
            self.hp_gain = hp_gain
            self.mp_gain = mp_gain
        def use(self, target, inventory):
            inventory.remove_item(self)
            target.add_hp(self.hp_gain)
            target.add_mp(self.mp_gain)

    class Equipable(StatItem):
        def __init__(self, name, img, value):
            StatItem.__init__(self, name, img, value)
            self.is_equipped = False
            self.equipped_to = None

        def equip(self, target):
            self.is_equipped = True
            self.equipped_to = target

        def unequip(self):
            self.is_equipped = False
            self.equipped_to = None

    class Weapon(Equipable):
        def __init__(self, name, img, value, atk, weapon_type):
            Equipable.__init__(self, name, img, value)
            self.atk = atk
            self.weapon_type = weapon_type

        def equip(self, target, inventory):
            Equipable.equip(self, target)
            target.equip_weapon(self, inventory)

        def unequip(self, inventory):
            character = self.equipped_to
            Equipable.unequip(self)
            character.unequip_weapon(inventory)

    class Armor(Equipable):
        def __init__(self, name, img, value, defense, mdef, slot):
            Equipable.__init__(self, name, img, value)
            self.defense = defense
            self.mdef = mdef
            self.slot = slot

        def equip(self, target, inventory):
            Equipable.equip(self, target)
            target.equip_armor(self, self.slot, inventory)

        def unequip(self, inventory):
            character = self.equipped_to
            Equipable.unequip(self)
            character.unequip_armor(self.slot, inventory)
