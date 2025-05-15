init python:
    class InventoryItem():
        def __init__(self, name, description):
            # Remember to save the values of the name and description
            "TODO"

        def __call__(self):
            return "TODO"

        def to_string(self):
            return "TODO"

    class Inventory():
        def __init__(self, character, items, item_count):
            self.items = items
            self.item_count = item_count
            self.character = character

        def add_item(self, item):
            self.items.append(item)
            self.item_count += 1

        def remove_item(self, item):
            # TODO
            "TODO"

        def say_items(self):
            # TODO
            "TODO"

    class ConsummableItem(InventoryItem):
        def __init__(self, name, hp_gain, mp_gain):
            InventoryItem.__init__(self, name, f"TODO: Write description")

