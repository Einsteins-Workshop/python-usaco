
label example_battle:
    default message = "Start of battle!"
    scene bg battle1
    call setup_monsters
    call setup_players
    show screen display_monsters with dissolve
    show screen battle_message
    show screen battle_overlay
    $ stop_narrative_mode()
    default inCombat = True
    default win = False
    while inCombat:
        python:
            for player in players:
                player.turn = False
                player.defending = False
        call turn_actions
        python:
             monster_turns(monsters, players)
             if not list(filter(is_alive, players)):
                 inCombat = False
    jump end_battle

label turn_actions:
    $ message = "Who will attack?"
    call screen turn_select
    $ current_player = _return
    if current_player != "done":
        call player_skill
        $ current_player.turn = True
        if inCombat == True:
            jump turn_actions
    else:
        $ current_player = None
        $ message = "Monsters are attacking."
        return
    return

label player_skill:
    call screen choose_skill
    $ skill = _return
    if skill == "attack":
        call choose_target
        # Damage one character
        $ message = f"{current_player.name} attacks {target.name} for {current_player.atk} damage!"
        $ attack(target, current_player.atk, current_player)
    elif skill == "defend":
        $ current_player.defending = True
    else:
        $ isSkill = isinstance(skill, MagicSkill)

        if isSkill and current_player.mp < skill.mp:
            $ message = "Not enough mp!"
            jump player_skill

        if isSkill and skill.aoe == False:
            call choose_target
            # Damage one character

            $ message = f"{current_player.name} uses {skill.description} on {target.name} for {2 * current_player.atk} damage!"
            $ attack(target, current_player.atk * 2, current_player)
            $ current_player.mp -= skill.mp
        elif isSkill and skill.aoe == True:
            # Damage all characters
            python:
                message = f"{current_player.name} uses {skill.description} on all monsters for {current_player.atk} damage!"
                for monster in monsters:
                    attack(monster, current_player.atk, current_player)
                current_player.mp -= skill.mp
    python:
         monsters = list(check_hp(monsters))
         if not monsters:
             message = "You win!"
             inCombat = False
             win = True
    return

label choose_target:
    message = "Pick a target"
    $ pick_target = True
    call screen select_monster
    $ target = _return
    $ pick_target = False
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

label setup_monsters:
    call load_monster_manual
    python:
        monsters = [monster_manual["lapras"], monster_manual["ditto"], monster_manual["eevee"], monster_manual["vaporeon"]]
        monster_slot_positions = [
            {
                "sprite_position": 0,
                "dmg_position": (576, 320)
            },
            {
                "sprite_position": 256,
                "dmg_position": (832, 320)
            },
            {
                "sprite_position": 0,
                "dmg_position": (576, 320)
            },
            {
                "sprite_position": 256,
                "dmg_position": (832, 320)
            }
        ]
    return

label end_battle:
    hide screen battle_overlay
    with dissolve
    if win:
        stop music
        play sound fanfare
        "You win!"
        stop sound
    else:
        $ message = "You Lost"
        "You lost..."
    hide screen battle_message
    hide screen display_monsters
