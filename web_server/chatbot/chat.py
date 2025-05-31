from flask import Flask, render_template, request, jsonify, session

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
    message = str(request.form['messageText'])
    if "name" in session:
        if session["state"] == ASKING:
            if message == 'Hi':
                bot_response = "Welcome to my lair"
            else:
                bot_response = "I haven't heard that before, how should I respond to that?"
                session["state"] = GET_ANSWER
        elif session["state"] == GET_ANSWER:
            bot_response = "I will totally not remember that."
            session["state"] = ASKING
        else:
            bot_response = f"MAJOR MALFUNCTION, UNKNOWN STATE {session['state']}"
    else:
        session["name"] = message
        bot_response = f"Hi {session['name']}, I am listening"
        session["state"] = ASKING
    print(bot_response)
    return jsonify({'status': 'OK', 'answer': bot_response})


if __name__ == "__main__":
    app.run()