# Import flask
from flask import Flask, jsonify
import hashlib
import requests
import json
from flask import Flask, request
import math
from redis import Redis
# Setup your app
slack_token = 'https://hooks.slack.com/services/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'
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.redis = Redis(host='redis',port=6379)

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

@app.route('/kv-retrieve/<id>', methods=['GET'])
def kv_retrieve(id):
    #Initialize JSON
    payload = {
        'input': id,
        'output' : False,
        'error' : 'N/A'
    }

    #Try Catch for Redis
    try:
        checkValue = app.redis.get(id)
    except:
        payload['error'] = "Cannot connect to redis"
        return jsonify(payload),400

    #Check for Value
    if checkValue == None:
        payload['error'] = "ID does not exist"
        return jsonify(payload),404
    else:
        payload['value'] = checkValue.decode("utf-8")

    payload['output'] = True
    return jsonify(payload), 200

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

#App route for Factorial
@app.route('/factorial/<string:userInput>')
def factorialfunction(userInput):
    userInput=int(userInput)
    if userInput<0:
        return jsonify(
            input=userInput,
            output="Error: You did not enter a positive integer")
    else :
      return jsonify(
      input=userInput,
      output=math.factorial(userInput)
    )

#Fibonacci Sequence
@app.route('/fibonacci/<int:userInput>')
def fibonaccifunction(userInput):
   results=[1,1]
   a=1
   if (userInput < 0):
       return jsonify(
            input=userInput,
            output="Error: Input is negative"
       )
   while(a<userInput):
       a=a+results[-2]
       if (a<userInput):
           results.append(a)
   return jsonify(
       input=userInput,
       output=results
   )

#App route for Prime number
@app.route('/is-prime/<int:userInput>')
def primefunction(userInput):
    prime = True
    i=2
    if (userInput>0):
        while(i<userInput):
            if(userInput%i==0):
                prime=False
            i+=1
        return jsonify(
            input=userInput,
            output=prime
        )
    else:
        return jsonify(
            input=userInput,
            output=false
        )

# This check will only run the code if you run it from the terminal, not if you import it
if __name__ == '__main__':
    # Set the debug = true
    app.debug = True
    # Run the app
    app.run('0.0.0.0')
