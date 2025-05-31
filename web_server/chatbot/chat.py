from flask import Flask, render_template, request, jsonify, session
import json
import os
import random

# Adapted from https://github.com/VRohit1901/ChatBot-Flask/
app = Flask(__name__)

app.secret_key = "xyzzy"
ASKING = 1
GET_ANSWER = 2


# A way of getting local files
# for file in os.listdir('C:/Users/Anonymous/Desktop/ChatBot-Flask/data/'):

#    chats = open('C:/Users/Anonymous/Desktop/ChatBot-Flask/data/' + file, 'r').readlines()


@app.route("/")
def hello():
    return render_template('chat.html')


@app.route("/clear", methods=['POST'])
def clear():
    session.clear()
    print("Clearing session cookies")
    return jsonify({'status': 'OK'})


@app.route("/ask", methods=['POST'])
def ask():
    # Greeting
    bot_response = "Critical error; Reload to fix"
    userInput = str(request.form['messageText'])
    print(session)
    print("name" in session)
    if "name" in session:
        votingThreshold = 0.5

        # File and folder setup
        folder = "userCATdata"
        if not os.path.exists(folder):
            os.makedirs(folder)

        filePath = os.path.join(folder, f"{session['name']}'s CAT data.json")

        # Load or initialize userInputs
        if os.path.exists(filePath):
            print(f"CAT: Nice to see you again, {session['name']}.")
            with open(filePath) as fileHandle:
                userInputs = json.load(fileHandle)
        else:
            userInputs = {}
            print(f"CAT: Nice to meet you, {session['name']}. I'm still learning, so please be patient with me.")

        # Load data from all user files to generate voting statistics
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        listOfDictionariesOfCATuserFiles = []
        for file in files:
            with open(os.path.join(folder, file)) as userFile:
                listOfDictionariesOfCATuserFiles.append(json.load(userFile))

        # Global dictionary to store vote counts
        userVotes = {}

        # Initialize votes
        # updateUserVotes()
        print("Just before state")
        if session["state"] == ASKING:
            print("ASKING")
            if userInput == "":
                bot_response = 'PlS TyPe sMtH In hErE'

            # If the input is recognized, print the stored response
            if userInput in userInputs:
                print("CAT:", userInputs[userInput])

                if userInput == 'Hi':
                    return response_string("Welcome to my lair")
                else:
                    session["state"] = GET_ANSWER
                    session["oldUserInput"] = userInput
                    return response_string("I haven't heard that from you before! What would be appropriate to say here? \nAppropriate response:")
        elif session["state"] == GET_ANSWER:

            print("GET_ANSWER")
            # Put in overwriteNewInput here
            session["state"] = ASKING
            userInputs[session["oldUserInput"]] = userInput
            with open(filePath, "w") as fileHandle:
                json.dump(userInputs, fileHandle)
        else:
            bot_response = f"MAJOR MALFUNCTION, UNKNOWN STATE {session['state']}"
    else:
        print("IN NAME")
        if userInput.strip() == "":
            bot_response = "Your name cannot be empty! \nYour name: "
        else:
            session["name"] = userInput
            bot_response = f"CAT: Nice to meet you, {session['name']}. I'm still learning, so please be patient with me."
            session["state"] = ASKING
    print(bot_response)
    return jsonify({'status': 'OK', 'answer': bot_response})

def response_string(answer):
    return jsonify({'status': 'OK', 'answer': answer})

if __name__ == "__main__":
    app.run()
