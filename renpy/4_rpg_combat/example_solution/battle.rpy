init python:
    from enum import Enum

    def start_narrative_mode():
        config.allow_skipping = True
        config.rollback_enabled = True
        renpy.choice_for_skipping()
        renpy.retain_after_load()
    def stop_narrative_mode():
        config.allow_skipping = False
        config.rollback_enabled = False
        renpy.block_rollback()
        renpy.choice_for_skipping()
        preferences.afm_enable = False

    class DamageType(Enum):
        ACID = 1
        FIRE = 2

    def can_target(monster, index):
        if renpy.get_screen("select_monster"):
            return True
        return False

    def attack(monster, damage, player):
        renpy.pause(0.2, hard = True)
        if monster.hp <= damage:
            monster.hp = 0
        else:
            monster.hp -= damage
        renpy.with_statement(hpunch)
        renpy.pause(0.2)
        return message

    def is_alive(character):
        return character.hp > 0

    def check_hp(characters):
        return filter(is_alive, characters)

    def monster_turns(monsters, characters):
        global monster_damage
        global hit_characters
        for monster in monsters:
            active_characters = list(filter(is_alive, characters))
            if not active_characters:
                return
            target = renpy.random.choice(active_characters)
            damage = max(1, monster.atk - target.defense)
            if target.defending:
                damage = round(damage/3)
            if damage > target.hp:
                monster_damage = target.hp
                target.hp = 0
            else:
                monster_damage = damage
                target.hp -= damage

            hit_characters = [target]
            renpy.show_screen("player_dmg")
            renpy.with_statement(hpunch)
            renpy.pause(1.0)
            renpy.hide_screen("player_dmg")
