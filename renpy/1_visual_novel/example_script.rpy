define lucy = Character("Lucy", color="#ffcccc")
define karah = Character("Karah", color="#ff0000")
define e = Character("Eitleen", color="ffcccc")

label start:

label example_game_dialog:

    "Karah" "Yo, I am the self-insert narrator of this game."
    "Wow, it is really dark here."
    "Karah" "Then turn on the dang lights!"
    "Karah" "That dawg thinks he is so \"smart\"."

    lucy "Hi, my name is Lucy!"

label example_game_images:
    scene bg town
    show karah smile
    karah "Hiyo."

    show eileen happy
    show sylvie blue normal at left
    show lucy happy at right
    show karah snide behind eileen
    karah "Where did all these girls come from?!"
    hide karah
    karah "Let's play hide and seek, bet you can't find me."

    hide eileen
    karah "There goes Eileen."
    hide sylvie
    karah "Never liked Sylvie neither."
    hide lucy
    show karah smile:
        xalign 0.25, yalign 1.0
    karah "Did ya miss me?"

    transform rightish:
        xalign 0.75
    show karah ready at rightish
    karah "See ya later aligator."

    scene bg town
    with Dissolve(.5)

    pause(.5)
    scene bg cave
    show eileen happy
    with Dissolve(.5)

    define slowdissolve = Dissolve(1.0)
    e "Here is an example slow dissolve"
    scene bg uni
    hide eileen
    with slowdissolve

    e "Here is an example slide"
    show eileen happy
    with slowdissolve
    show eileen happy at right
    with move
    e "I'm happier over here"

label example_game_sounds:
    play music "audio/milky-chu_ohchootrain.ogg" fadeout 1
    karah "Here is some music."
    queue music "audio/sunflower-slow-drag.ogg"
    karah "Queuing some carnival music, you may have to wait a while for the old music to finish."
    stop music fadeout 1
    karah "Stopping the music."
    play sound "audio/tower_clock.ogg"
    queue sound "audio/tower_clock.ogg"
    queue sound "audio/tower_clock.ogg"
    karah "tolling the clock"

label example_game_choices:
    scene bg uni
    show eileen happy
menu choice1:
    "I choose you Pikachu":
        jump choice1_pikachu
    "I choose you Squirtle":
        jump choice1_squirtle
label choice1_pikachu:
    $ pokemon = "Pikachu"
    show pikachu upright:
        xalign 0.5, yalign 0.5
    "Pikachu" "Pika Pika"
    jump choice1_done
label choice1_squirtle:
    show squirtle upright:
        xalign 0.5, yalign 0.5
    "Squirtle" "Sqrtl"
    $ pokemon = "Squirtle"
    jump choice1_done
label choice1_done:
    show eileen happy at right
    with move
    e "You chose [pokemon]"
    e "Say goodnight to [pokemon]"
    if pokemon == "Pikachu":
        hide pikachu
    else:
        hide squirtle

label example_interpolation:
    scene bg cave
    show eileen happy
python:
    player_name = renpy.input("What is your name?")
    player_name = player_name.strip() or "Guy d'Epee"

label name_display:
    define p = Character("[player_name]")
    e "Welcome [player_name]"
    p "The last thing I remeber was the flash of lightning"
