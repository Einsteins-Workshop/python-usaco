init python:
    class Monster():
        def __init__(self, name, img, anim, hp, atk):
            self.name = name
            self.img = img
            self.anim = anim
            self.max_hp = hp
            self.hp = hp
            self.atk = atk

    global monster_manual

    def _shake_function(trans, st, at, dt=.5, dist=64):
        if st <= dt:
            trans.xoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            trans.yoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            return 1.0/60
        else:
            return None

define move_time = .5
define stand_anchor = (.5, .5)
define move_size = 10

transform idle_shake(t=move_time, d=move_size, a=stand_anchor):
    pause renpy.random.randint(3,6)
    function renpy.curry(_shake_function)(dt=t, dist=d/2)
    xoffset 0 yoffset 0
    renpy.random.randint(1,3)
    repeat

transform idle_y(t=move_time, d=move_size, a=stand_anchor):
    ease t yoffset -d
    ease t yoffset 0
    repeat

transform slow_sway(e=1.2):
    easein e xoffset -20
    pause e
    easein e xoffset 20
    pause e
    repeat


transform shake_fade(t=move_time, d=move_size):
    function renpy.curry(_shake_function)(dt=t, dist=d*2)
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        parallel:
            linear .25 alpha 0.0
        parallel:
            linear .25 zoom 1.5
    xoffset 0 yoffset 0

init python:
    def _shake_function(trans, st, at, dt=.5, dist=64):
        if st <= dt:
            trans.xoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            trans.yoffset = int((dt-st)*dist*(.5-renpy.random.random())*2)
            return 1.0/60
        else:
            return None

transform squeeze:
    pause renpy.random.randint(3,6)
    parallel:
        ease 0.3 yzoom 1.2
        ease 0.3 yzoom 1
        pause 0.2
    parallel:
        easein 0.3 yoffset -60
        easeout 0.3 yoffset 0
        ease 0.1 yoffset -3
        ease 0.1 yoffset 0
    parallel:
        ease 0.3 xzoom 0.7
        ease 0.3 xzoom 1
        pause 0.2
    repeat

label load_monster_manual:
    python:
        monster_manual = {
            "lapras": Monster("Lapras", "lapras.png", slow_sway, 20, 8),
            "ditto": Monster("Ditto", "ditto.png", squeeze, 50, 10),
            "eevee": Monster("Eevee", "eevee.png", idle_shake, 30, 10),
            "vaporeon": Monster("Vaporeon", "vaporeon.png", idle_y, 25, 12)
        }
