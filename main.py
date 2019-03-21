# Import flask
from flask import Flask, jsonify
import hashlib
import requests
import json
from flask import Flask, request

# Setup your app
slack_token = 'https://hooks.slack.com/services/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'
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
    return jsonify(
        input=message,
        output=True
    )

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
def fibonaccifunction(userInput):
   results=[1,1]
   a=1
   if (userInput < 0)
        return jsonify(
       input=userInput,
       output="wrong input"
   )
   while(a<userInput):
       a=a+results[-2]
       if (a<userInput):
           results.append(a)
   return jsonify(
       input=userInput,
       output=results
   )


@app.route('/is-prime/<int:userInput>')
def is_prime(userInput):
    try:
        userInput += 1
    except TypeError:
        return jsonify(
            input = userInput,
            error = "invalid input, input must be an int"
        )
    if userInput >= 2:
        for x in range(2,userInput):
            #if divisible, return false
            if not(userInput % x):
                return False
    else:
        return False
    return True



# This check will only run the code if you run it from the terminal, not if you import it
if __name__ == '__main__':
    # Set the debug = true
    app.debug = True
    # Run the app
    app.run('0.0.0.0')
