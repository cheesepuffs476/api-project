#Import flask
from flask import Flask, jsonify
import hashlib
import requests
import json
from flask import Flask, request

#Setup app
slack_token = 'https://hooks.slack.com/services/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'
app = Flask(__name__)

#Set up route
@app.route('/')
def index():
    # Do cool shit here
    return 'it works'

#Additional routes
@app.route('/md5/<string:userInput>')
def hashfunction(userInput):
    hash_object = hashlib.md5(userInput.encode())
    return jsonify(
        input=userInput,
        output=hash_object.hexdigest()
    )

#Slack Alerts
@app.route('/slack-alert/<string:message>')
def send_to_slack(message):
    payload = {'text': message}
    requests.post(slack_token, json.dumps(payload))
    return 'True'

#Endpoint returns factorial for integer that is inputted. If integer is not positive, error message will be displayed
@app.route('/factorial/<string:userInput')
def factorialfunction(userInput):
    if userInput==1 :
                  return userInput
     else :

           ethelse = userInput(userInput-1)
           return ethelse
    )

#An array of integers with all Fibonacci numbers less than or equal to the input  will be outputted. If the integer is not positive, error message will be displayed
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

#A boolean value will be returned depending on whether the input is a prime number. If the input is invalid, error message will be displayed
@app.route('/is-prime/<int:userInput>')
def is_prime(userInput):
    if isinstance(userInput,int):
        prime = True
        if userInput < 2:
            prime = False
            return jsonify(
                input= userInput,
                output= 'Input is not prime'
            )
        else:
            for n in range(2, userInput):
                if userInput % n == 0:
                    prime = False
                    break
                else:
                    prime = True
                    return jsonify(
                        input= userInput,
                        output= 'Input is prime'
                    )
    else:
        return jsonify(
            input= userInput,
            output= 'Input must be integer'
        )
            # divisible, return

# This check will only run the code if you run it from the terminal, not if it is imported
if __name__ == '__main__':
    # Set the debug = true
    app.debug = True
    # Run the app
    app.run('0.0.0.0')
