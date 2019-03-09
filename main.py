# Import flask
from flask import Flask, jsonify
import hashlib
import requests
import json
from flask import Flask, request

# Setup your app
slack_token = ''
app = Flask(__name__)

# Set up a route
@app.route('/')
def index():
    # Do cool shit here
    return 'it works'

# More routes go here...
@app.route('/md5/<string:userInput>')
def hashfunction(userInput):
    hash_object = hashlib.md5(userInput.encode())
    return jsonify(
        input=userInput,
        output=hash_object.hexdigest()
    )

#Slack Alert
@app.route('/slack-alert/<string:message>')
def send_to_slack(message):
    payload = {'text': message}
    requests.post(slack_token, json.dumps(payload))
    return 'True'

#@app.route('/factorial/<string:userInput')
#def factorialfunction(userInput):
#    if userInput==1 :
#                  return userInput
#     else :
#
#           ethelse = userInput(userInput-1)
#           return ethelse
#    )
@app.route('/fibonacci/<int:userInput>')
def hashfunction(userInput):
    hash_object = hashlib.md5(userInput.encode())
    return jsonify(
        input=userInput,
        output=hash_object.hexdigest()
    )





# This check will only run the code if you run it from the terminal, not if you import it
if __name__ == '__main__':
    # Set the debug = true
    app.debug = True
    # Run the app
    app.run('0.0.0.0')
