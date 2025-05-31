init python:
    class InventoryItem():
        def __init__(self, name, description):
            self.name = name
            self.description = description

        def __call__(self):
            return self.to_string()

        def to_string(self):
            return f"{self.name} - {self.description}"


    class StatItem(InventoryItem):
        def __init__(self, name, img, value):
            self.name = name
            self.img = img
            self.value = value
        def __call__(self):
            return self.to_string()

        def to_string(self):
            return f"TODO"

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

    class Consumable(StatItem):
        def __init__(self, name, img, value, regen, regain):
            StatItem.__init__(self, name, img, value)
            self.regen = regen
            self.regain = regain

        def consume(self, target, inventory):
            target.add_hp(self.regen)
            inventory.remove_item(self)


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
