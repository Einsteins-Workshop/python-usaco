style inventory_text is gui_text:
    size 15
    color "#000000"

screen hud():
    modal False

    imagebutton auto "bg hud inventory %s.png":
        hovered SetVariable("screen_tooltip", "Inventory")
        unhovered SetVariable("screen_tooltip", "")
        action Show("inventory"), Hide("hud")

screen inventory():
    add "bg inventory"
    modal True

    vbox:
        pos 0.2, 0.25
        for item in inventory.items:
            $ item_description = item.to_string()
            text "[item_description]\n" style "inventory_text"

    imagebutton auto "bg hud inventory %s.png":
        hovered SetVariable("screen_tooltip", "Return")
        unhovered SetVariable("screen_tooltip", "")
        action Show("hud"), Hide("inventory")