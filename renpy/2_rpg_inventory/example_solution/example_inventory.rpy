init python:
    class InventoryItem():
        def __init__(self, name, description):
            self.name = name
            self.description = description

        def __call__(self):
            return self.to_string()

        def to_string(self):
            return f"{self.name} - {self.description}"

    class Inventory():
        def __init__(self, character, items, item_count):
            self.items = items
            self.item_count = item_count
            self.character = character

        def add_item(self, item):
            self.items.append(item)
            self.item_count += 1

        def remove_item(self, item):
            self.items.remove(item)
            self.item_count -= 1

        def say_items(self):
            if (self.item_count) < 1:
                say(self.character, "I'm not carrying anything.")
            else:
                say(self.character, "I'm currently carrying:")
                for item in self.items:
                    say(self.character, item())

    class ConsummableItem(InventoryItem):
        def __init__(self, name, hp_gain, mp_gain):
            self.hp_gain = hp_gain
            self.mp_gain = mp_gain
            InventoryItem.__init__(self, name, f"Consume to gain {hp_gain} hp and {mp_gain} mp")

    class LootItem(InventoryItem):
        def __init__(self, name, value):
            self.value = value
            InventoryItem.__init__(self, name, f"Worth {self.value} gold pieces")
