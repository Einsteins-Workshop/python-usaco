from flask import Flask, render_template, request, jsonify, session
import json
import os
import random

app = Flask(__name__)
app.secret_key = "xyzzy"  # Needed for sessions

ASKING = 1
GET_ANSWER = 2

@app.route("/")
def render():
    return render_template('chat.html')

@app.route("/clear", methods=['POST'])
def clear():
    session.clear()
    print("Clearing session cookies")
    return jsonify({'status': 'OK'})

@app.route("/ask", methods=['POST'])
def ask():
    userInput = str(request.form['messageText']).strip()
    print("Session:", session)

    if "name" not in session:
        if userInput == "":
            return jsonify({'status': 'OK', 'answer': "Your name cannot be empty! \nYour name: "})
        session["name"] = userInput
        session["state"] = ASKING
        return jsonify({'status': 'OK', 'answer': f"CAT: Nice to meet you, {session['name']}. I'm still learning, so please be patient with me."})

    folder = "userCATdata"
    os.makedirs(folder, exist_ok=True)
    filePath = os.path.join(folder, f"{session['name']}'s CAT data.json")

    if os.path.exists(filePath):
        with open(filePath) as fileHandle:
            userInputs = json.load(fileHandle)
        print("Loaded userInputs:", userInputs)
    else:
        userInputs = {}
        print("New user")

    if session["state"] == ASKING:
        if userInput == "":
            return response_string("PlS TyPe sMtH In hErE")
        elif userInput in userInputs:
            return response_string(userInputs[userInput])
        else:
            session["state"] = GET_ANSWER
            session["oldUserInput"] = userInput
            return response_string("I haven't heard that from you before! What would be appropriate to say here? \nAppropriate response:")

    elif session["state"] == GET_ANSWER:
        userInputs[session["oldUserInput"]] = userInput
        with open(filePath, "w") as fileHandle:
            json.dump(userInputs, fileHandle)
        print(f"Saved: {session['oldUserInput']} -> {userInput}")
        session["state"] = ASKING
        return response_string("Thanks! I'll remember that for next time.")

    return response_string(f"MAJOR MALFUNCTION, UNKNOWN STATE {session.get('state')}")

    return jsonify({'status': 'OK', 'answer': bot_response})

def response_string(answer):
    return jsonify({'status': 'OK', 'answer': 'CAT: '+answer})

if __name__ == "__main__":
    app.run(debug=True)
