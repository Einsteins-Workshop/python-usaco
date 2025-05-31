from flask import Flask
app = Flask(__name__)

# This webserver uses the Flask framework

# To run this webserver, you can run the following command line:
# python -m flask —app test_app run.

# You can als run within PyCharm by creating a special configuration, with
# module = flask
# parameters = —app test_app_run
# working directory being the web_server directory

@app.route('/')
def hello():
    return f'Hello, Little One!  Where would you like to go?'