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

    add "a white_area.png"
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
                    textbutton "Use" action Function(selected_item.use, selected_character, inventory), SetVariable("selected_item", None)
                if isinstance(selected_item, Equipable):
                    textbutton "Equip" action Function(selected_item.equip, selected_character, inventory), SetVariable("selected_item", None)
                textbutton "Discard" action Function(inventory.remove_item, selected_item), SetVariable("selected_item", None)

    textbutton "Return":
        action Show("characters"), Hide("character_sheet")
        xalign 0.5
        yalign 0.95