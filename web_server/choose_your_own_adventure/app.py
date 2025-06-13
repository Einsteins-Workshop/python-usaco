from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

# This example is inspired from
# https://github.com/x/starter-flask-app-choose-your-own-adventure/blob/main/templates/page.html

app.secret_key = "xyzzy"

@app.route('/')
def page_1():
    session["found_keys"] = False
    text = """
    You’re sitting at your desk writing your own computer program, when you are sucked into your program and find
    yourself in an underground bunker. You leave your bare cell, and find a corridor going to the left and to the right.
    """
    choices = [
        {"text": "Go to the left", "route": "page_2"},
        {"text": "Go to the right", "route": "page_3"},
    ]
    return render_template('page.html', content=text, choices=choices)


@app.route('/page_2')
def page_2():
    text = """
    You go down the left hallway and follow the turn to a door. As you enter the room, you find a security office with a
     set of monitors.  There is a also a weapons locker that has been previously broken into.
    """
    choices = [
        {"text": "Leave the room and pass your cell to try the right passage", "route": "page_3"},
        {"text": "Look at the computer", "route": "page_4"},
        {"text": "Rummage through the locker", "route": "page_5"},

    ]
    return render_template('page.html', content=text, choices=choices)

@app.route('/page_3', methods=['GET', 'POST'])
def page_3():
    if request.method == 'POST':
        return page_3_post()
    text = '''
    You go down the right hallway and follow the turn to a door. After opening it, you find yourself
    in a garage, confronted by an angry looking robot who says in a low monotone, "State the passcode or be
    vaporized"
    '''
    input_text = "Say the code out loud"
    choices = [
        {"text": "Run away", "route": "page_7"},
    ]
    return render_template('text_box_page.html', content=text, choices=choices, input=input_text)

def page_3_post():
    text = request.form['text'].lower()
    if text.startswith('have a nice day'):
        story_text = """
        The robot ignores you, leaving you alone in the garage, with the garage door to the outside closed.  There is a 
        jeep in the garage.
        """
        choices = [
            {"text": "Leave the room and pass your cell to try the left passage", "route": "page_2"},
            {"text": "Examine the jeep", "route": "page_6"},
        ]

        return render_template('page.html', content=story_text, choices=choices)
    return redirect("page_7")



@app.route('/page_4')
def page_4():
    text = """
    The monitors shows the empty cell that you were originally in and a garage with a jeep, guarded by a nasty looking 
    robot. There is also a third room shown, with a poster of the infamous alien cyborg Zaphod Buzzkill saying "If you
    want to live, say have a nice day!"
    """
    choices = [
        {"text": "Look around this room", "route": "page_2"},
        {"text": "Leave the room and pass your cell to try the right passage", "route": "page_3"},
    ]
    return render_template('page.html', content=text, choices=choices)


@app.route('/page_5')
def page_5():
    if not(session["found_keys"]):
        text = """
        You look for something useful in the locker, but it looks like it is already ransacked. After searching through
        someone's stinky socks, you find a key ring with a car key.
        """
        session["found_keys"] = True
    else:
        text = """
        You find nothing else of interest in the locker.
        """
    choices = [
        {"text": "Look around this room", "route": "page_2"},
        {"text": "Leave the room and pass your cell to try the right passage", "route": "page_3"},
    ]
    return render_template('page.html', content=text, choices=choices)

@app.route('/page_6')
def page_6():
    choices = [
        {"text": "Leave the room and pass your cell to try the left passage", "route": "page_2"},
    ]
    if not(session["found_keys"]):
        text = """
        The jeep is firmly locked.  You try to jimmy open the lock, but fail.
        """
        choices.append({"text": "Try to force open the jeep lock again", "route": "page_6"})
    else:
        text = """
        The car keys fit the jeep.  You find a garage door opener inside the car as well. Sweet!
        """
        choices.append({"text": "Get out of here", "route": "page_8"})
    return render_template('page.html', content=text, choices=choices)


@app.route('/page_7')
def page_7():
    text = """
    The robot says, "Unauthorized intruder" and aims its plasma armanents at you.  You are vaporized.
    <br><br>
    <b>Bad Ending: Game Over.</b>
    """
    choices = [
        {"text": "Start Over", "route": "/"},
    ]
    reset_game()
    return render_template('page.html', content=text, choices=choices)

@app.route('/page_8')
def page_8():
    text = """
    You open the garage and stare out into the glaring desert sun.  You then drive out to find your way back home.
    <br><br>
    <b>Good Ending: You Emerge Triumphant.</b>
    """
    reset_game()
    choices = [
        {"text": "Start Over", "route": "/"},
    ]
    return render_template('page.html', content=text, choices=choices)

def reset_game():
    session["found_keys"] = False