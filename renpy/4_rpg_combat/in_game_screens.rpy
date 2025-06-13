init python:
    style.bar_mhp = Style(style.default)
    style.bar_mhp.left_bar = Frame("images/mp_full.png",20,20)
    style.bar_mhp.right_bar = Frame("images/mp_empty.png",20,20)
    style.bar_mhp.xmaximum = 180
    style.bar_mhp.ymaximum = 25

    style.bar_hp = Style(style.default)
    style.bar_hp.left_bar = Frame("images/hp_full.png",20,20)
    style.bar_hp.right_bar = Frame("images/hp_empty.png",20,20)
    style.bar_hp.xmaximum = 213
    style.bar_hp.ymaximum = 40

    style.bar_mp = Style(style.default)
    style.bar_mp.left_bar = Frame("images/mp_full.png",20,20)
    style.bar_mp.right_bar = Frame("images/mp_empty.png",20,20)
    style.bar_mp.xmaximum = 213
    style.bar_mp.ymaximum = 40

style inventory_text is gui_text:
    size 15
    color "#000000"

style character_sheet_label:
    xalign 0.2

style slot:
    background Frame("slot", 0, 0)
    minimum(40, 40)
    maximum(40, 40)
    xalign 0.5

style battle_playername_text:
    font "gui/prstart.ttf"
    outlines [(4, "#00000025", 2, 2), (2, "#900c3f", 0, 0)]
    color "#ff5733"
    size 24

style battle_playerlvl_text:
    font "gui/prstart.ttf"
    color "#ffffff"
    outlines [(2, "#00000080", 1, 1)]
    size 16

style dmg_text:
    font "gui/earwig.ttf"
    color "#000000"
    size 80
    outlines [(4.5, "#ffffff", 3.5, 3.5)]

screen characters():
    modal False
    vbox:
        imagebutton auto "chie icon %s.png":
            action SetVariable("selected_character", chie), Show("character_sheet"), Hide("characters")
        imagebutton auto "yu icon %s.png":
            action SetVariable("selected_character", yu), Show("character_sheet"), Hide("characters")


screen character_sheet():
    modal True
    style_prefix "character_sheet"

    add "white"
    hbox:
        spacing 100
        vbox:
            xmaximum 300
            spacing 10
            add "[selected_character.img_icon]"
            label "Level [selected_character.level]"
            label "Character Stats" xalign 0.5
            label "HP: [selected_character.hp]/[selected_character.max_hp]"
            label "MP: [selected_character.mp]/[selected_character.max_mp]"
            label "Attack: [selected_character.atk]"
            label "Defense: [selected_character.defense]"
            label "Magic Defense: [selected_character.mdef]"

        vbox:
            spacing 10
            label "Equipped Items"

            label "Weapon"
            frame:
                style "slot"
                if selected_character.weapon != None:
                    add selected_character.weapon.img

            if selected_character.weapon != None:
                textbutton "Unequip" action Function(selected_character.weapon.unequip, inventory)

            label "Helmet"
            frame:
                style "slot"
                if selected_character.armor["head"] != None:
                    add selected_character.armor["head"].img
            if selected_character.armor["head"] != None:
                textbutton "Unequip" action Function(selected_character.armor["head"].unequip, inventory)

            label "Armor"
            frame:
                style "slot"
                if selected_character.armor["chest"] != None:
                    add selected_character.armor["chest"].img
            if selected_character.armor["chest"] != None:
                textbutton "Unequip" action Function(selected_character.armor["chest"].unequip, inventory)

            label "Accessory"
            frame:
                style "slot"
                if selected_character.armor["acc"] != None:
                    add selected_character.armor["acc"].img
            if selected_character.armor["acc"] != None:
                textbutton "Unequip" action Function(selected_character.armor["acc"].unequip, inventory)

            label "Shield"
            frame:
                style "slot"
                if selected_character.armor["shield"] != None:
                    add selected_character.armor["shield"].img
            if selected_character.armor["shield"] != None:
                textbutton "Unequip" action Function(selected_character.armor["shield"].unequip, inventory)

        grid 10 14:
            yalign 0.2
            spacing 5
            for item in inventory.displayable_items:
                frame:
                    style "slot"
                    imagebutton idle item.img action SetVariable("selected_item", item)
            for i in range(len(inventory.displayable_items), 140):
                frame:
                    style "slot"

        vbox:
            spacing 10
            label "Current Item" xalign 0.5
            if selected_item != None:
                label selected_item.name
                frame:
                    style "slot"
                    add selected_item.img
                label "Value: [selected_item.value]"
                if isinstance(selected_item, Consummable):
                    textbutton "Use" action Function(selected_item.use, selected_character, inventory)
                if isinstance(selected_item, Equipable):
                    textbutton "Equip" action Function(selected_item.equip, selected_character, inventory)
                textbutton "Discard" action Function(inventory.remove_item, selected_item)

    textbutton "Return":
        action Show("characters"), Hide("character_sheet")
        xalign 0.5
        yalign 0.95

screen display_monsters_no_targeting():
    fixed:
        pos (800, 300)
        for idx, monster in enumerate(monsters[0:2]):
            fixed:
                xpos monster_slot_positions[idx]["sprite_position"]
                imagebutton at monster.anim:
                    hover im.MatrixColor(monster.img, im.matrix.brightness(0.1))
                    action Return(monster)
                    idle monster.img anchor (0.5, 1.0)
                bar style "bar_mhp" value AnimatedValue(value = monster.hp, range = monster.max_hp, delay = 0.25) anchor (0.5, 1.0)
                text "[monster.hp]" xanchor 0.5

    fixed:
        pos (800, 600)
        for idx, monster in enumerate(monsters[2:4]):
            fixed:
                xpos monster_slot_positions[idx]["sprite_position"]
                imagebutton at monster.anim:
                    hover im.MatrixColor(monster.img, im.matrix.brightness(0.1))
                    idle monster.img anchor (0.5, 1.0)
                bar style "bar_mhp" value AnimatedValue(value = monster.hp, range = monster.max_hp, delay = 0.25) anchor (0.5, 1.0)
                text "[monster.hp]" xanchor 0.5


screen display_monsters():
    fixed:
        pos (800, 300)
        for idx, monster in enumerate(monsters[0:2]):
            fixed:
                xpos monster_slot_positions[idx]["sprite_position"]
                imagebutton at monster.anim:
                    hover im.MatrixColor(monster.img, im.matrix.brightness(0.1))
                    action Return(monster), SensitiveIf(can_target(monster, idx))
                    idle monster.img anchor (0.5, 1.0)
                bar style "bar_mhp" value AnimatedValue(value = monster.hp, range = monster.max_hp, delay = 0.25) anchor (0.5, 1.0)
                text "[monster.hp]" xanchor 0.5

    fixed:
        pos (800, 600)
        for idx, monster in enumerate(monsters[2:4]):
            fixed:
                xpos monster_slot_positions[idx]["sprite_position"]
                imagebutton at monster.anim:
                    hover im.MatrixColor(monster.img, im.matrix.brightness(0.1))
                    action Return(monster), SensitiveIf(can_target(monster, idx))
                    idle monster.img anchor (0.5, 1.0)
                bar style "bar_mhp" value AnimatedValue(value = monster.hp, range = monster.max_hp, delay = 0.25) anchor (0.5, 1.0)
                text "[monster.hp]" xanchor 0.5

screen battle_message():
    add "images/messagebox.png"
    hbox:
        xpos 110 yalign 0.07
        text message

screen battle_overlay():
    fixed:
        xoffset 0
        for idx, character in enumerate(players):
            imagebutton:
                focus_mask True
                yalign 1.1 xpos player_slot_positions[idx]["img_pos"]
                idle character.img_battle
            fixed:
                pos player_slot_positions[idx]["bar_pos"], 200
                vbox:
                    text "[character.name]" anchor (1.0, 1.0) xoffset 110 style "battle_playername_text"
                    text "LVL.[character.level]" anchor (1,0, 1,0) xoffset 110 style "battle_playerlvl_text"
                    fixed:
                        yoffset -40
                        bar style "bar_hp" value AnimatedValue(value = character.hp, range = character.max_hp, delay=0.25) xanchor .5
                        bar style "bar_mp" value AnimatedValue(value = character.mp, range = character.max_mp, delay=0.25) xanchor .5 yalign 0.05
                        text "[character.hp]/[character.max_hp]" xanchor .5 yalign 0.0075
                        text "[character.mp]/[character.max_mp]" xanchor .5 yalign 0.0575



screen choose_skill():
    # The user can left click out of a turn to exit
    key "mouseup_3" action Function(renpy.pop_call), Jump("turn_actions")
    add "images/skillbox.png" pos 8, 214
    vbox:
        align (0.35, 0.40)
        textbutton "Attack" align (0.5, 0.5) action Return("attack")
        textbutton "Defend" align (0.5, 0.5) action Return("defend")
        textbutton "[current_player.magic_attack.description]- [current_player.magic_attack.mp] MP" align (0.5, 0.5) action Return(current_player.magic_attack)
        textbutton "Cancel" align (0.5, 0.5) action Function(renpy.pop_call), Jump("turn_actions")

screen select_monster():
    key "mouseup_3" action Function(renpy.pop_call), Jump("player_skill")
    frame:
        yalign 0.2
        has vbox:
            textbutton "Cancel" xalign 0.5 action Function(renpy.pop_call), Jump("player_skill")


screen turn_select():
    frame:
        yalign 0.2
        has vbox:
            for player in players:
                if not player.turn and player.hp > 0:
                    textbutton "[player.name]" xalign 0.5 action Return(player)
            textbutton "End Turn" xalign 0.5 action Return("done")

screen player_dmg():
    style_group "dmg"
    for p in hit_characters:
        text "[monster_damage]" anchor (.5,.5) xpos p.dmg_pos ypos 200 at shake_fade
    timer 1 action Hide('player_dmg')
