#Import flask
from flask import Flask, jsonify
import hashlib
import requests
import json
from flask import Flask, request

#Setup apps
slack_token = 'https://hooks.slack.com/services/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'
=======
import math
from redis import Redis
slack_token = 'https://hooks.slack.com/services/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'

app = Flask(__name__)
app.redis = Redis(host='redis',port=6379)

#Value posted to the URL will be recorded and saved in datastore attached to key supplied by URL. Only HTTP methods "POST" AND "PUT" are accepted by this URL. The output returns a boolean value that shows success. If it is false, an error message will be displayed
@app.route('/kv-record/<id>',methods=["POST","PUT"])
def create_post(id):
    data = request.data.decode('utf-8')
    checkValue = app.redis.get(id)
    if(checkValue==None) and (request.method=="PUT"):
        return  jsonify(
            input=id,
            output=False,
            error="Can't update value. Value doesn't exist"
        ),400
    elif (not checkValue == None) and (request.method=="POST"):
        return  jsonify(
            input=id,
            output=False,
            error="Value already exists"
        ),400
    elif (not checkValue == None) and (request.method=="PUT"):
        app.redis.set(id,data)
        return jsonify(
            input=id,
            output=True
        )
    if checkValue == True:
        app.redis.set(id,data)
        return jsonify(
            input=id,
            output=True
        )
    app.redis.set(id,data)
    return jsonify(
        input=id,
        output=True,
    )

#Values associated with the key supplied in the URL will be retrieved. The output will display value if successful or "false" if unsuccessful as well as an error message that indicates why the retrieval failed
@app.route('/kv-retrieve/<id>', methods=['GET'])
def kv_retrieve(id):
    #Initialize JSON
    payload = {
        'Input': id,
        'Output' : False,
        'Error' : 'N/A'
    }

#Set up route
@app.route('/')
def index():
    # Do cool shit here
    return 'it works'

#Additional routes

    #Try Catch for Redis
    try:
        checkValue = app.redis.get(id)
    except:
        payload['Error'] = "Cannot connect to redis"
        return jsonify(payload),400

    #Check for Value
    if checkValue == None:
        payload['Error'] = "ID does not exist"
        return jsonify(payload),404
    else:
        payload['Value'] = checkValue.decode("utf-8")

    payload['Output'] = True
    return jsonify(payload), 200

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

#Endpoint returns factorial for integer that is inputted. If integer is not positive, an error message will be displayed
@app.route('/factorial/<string:userInput')
def factorialfunction(userInput):
    if userInput==1 :
                  return userInput
     else :

           ethelse = userInput(userInput-1)
           return ethelse
    )

#An array of integers with all Fibonacci numbers less than or equal to the input  will be outputted. If the integer is not positive, an error message will be displayed
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

#A boolean value will be returned depending on whether the input is a prime number. If the input is invalid, an error message will be displayed
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
