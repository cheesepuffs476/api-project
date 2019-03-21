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





nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

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
