# Classes in python are used to create code separation. This can be useful both as a way to reuse
# the same code (similar to how we use functions and loops), keep all the relevant code in one place
# for easier organization, and as a convenient pattern so that our code is easy to read and understand.
#
# Classes are templates for the creation of objects. These newly created objects can store data and
# run the functions definted in the classes.
#
# Classes are often in their own modules and are imported using 'import' and/or 'from' statements. See
# https://realpython.com/lessons/import-statement/ for more info
#
#

class Character:
    # The __init__ function is a special function that creates an object. You can pass parameters to
    # represent initial data, and is by convention stored to self.
    def __init__(self, type, hp, attack, defense):
        self._type = type
        self._hp = hp
        self._attack = attack
        self._defense = defense

    # All functions need an initial parameter which represents this object, which is called by
    # convention self. The "self" parameter does not need to be called, and is implicit with the
    # object.method() call method for objects.
    def is_alive(self):
        return self._hp > 0

    def attack(self, other_character):
        # Note that class functions (called methods) are called by calling the object with the . operator
        if self.is_alive():
            other_character.take_damage(self._attack)

    def take_damage(self, damage):
        if self._hp <= damage:
            self._hp = 0
        else:
            self._hp -= damage

    def print_status(self):
        if self.is_alive():
            print(f"This {self._type} has {self._hp} hit points remaining.")
        else:
            print(f"This {self._type} is dead")


orc = Character("orc", 10, 5, 3)
wolf = Character("wolf", 3, 1, 0)
orc.attack(wolf)

print("For orc:")
orc.print_status()

print("For wolf:")
wolf.print_status()


# Classes can be based on other classes, and inherits all the methods of that class by default.
class PlayerCharacter(Character):
    def __init__(self, name, hp, attack, defense):
        self._name = name
        # This calls the Character.__init__ method
        super().__init__("pc", hp, attack, defense)

    # This overwrites the behavior of print_status
    def print_status(self):
        if self.is_alive():
            print(f"{self._name} has {self._hp} hit points remaining.")
        else:
            print(f"{self.name} is dead")


gimli = PlayerCharacter("Gimli", 20, 10, 4)
gimli.attack(orc)
print("After Gimli attacks the orc:")
orc.print_status()

gimli.print_status()
