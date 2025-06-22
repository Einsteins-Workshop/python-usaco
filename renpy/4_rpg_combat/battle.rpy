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

    def can_target(monster, index):
        if renpy.get_screen("select_monster"):
            return True
        return False