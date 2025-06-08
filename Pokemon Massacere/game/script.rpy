label start:
    default message = "Start of battle!"

    call setup_monsters
    show screen display_monsters_no_targeting with dissolve
    call setup_players
    show screen battle_overlay
    scene bg battle1
    "PAUSE"

label setup_monsters:
    call load_monster_manual
    python:
        monsters = [monster_manual["lapras"], monster_manual["eevee"], monster_manual["vaporeon"], monster_manual["ditto"]]
        monster_slot_positions = [
            {
                "sprite_position": 0,
                "dmg_position": (576, 320)
            },
            {
                "sprite_position": 200,
                "dmg_position": (832, 320)
            },
            {
                "sprite_position": 0,
                "dmg_position": (576, 320)
            },
            {
                "sprite_position": 300,
                "dmg_position": (832, 320)
            }
        ]
    return

label setup_players:
    python:
        water_bolt = MagicSkill(1, DamageType.ACID, "Water bolt")
        fire_ball = MagicSkill(2, DamageType.FIRE, "Fire ball", aoe = True)
        chie = PlayerCharacter(110, 5, 6, 3, 2, "chie", water_bolt, 1)
        yu = PlayerCharacter(102, 4, 4, 5, 5, "yu", fire_ball, 1)
        players = [chie, yu]
        player_slot_positions = [
            {
                "img_pos": 0,
                "bar_pos": 150,
                "dmg_pos": 250
            },
            {
                "img_pos": 300,
                "bar_pos": 500,
                "dmg_pos": 600
            }
        ]
        for count, player in enumerate(players):
            player.dmg_pos = player_slot_positions[count]["dmg_pos"]

    return