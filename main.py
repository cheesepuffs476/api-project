#Import flask
from flask import Flask, jsonify
import hashlib
import requests
import json
from flask import Flask, request
import math
from redis import Redis

#Setup apps
slack_token = 'https://hooks.slack.com/services/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'
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.redis = Redis(host='redis',port=6379)

#Default route for troubleshooting
@app.route('/')
def helloworld():
    return "Hello World. This is a test of the CI/CD Pipeline with GitLab. Testing"


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

#Endpoint will return the MD5 hash of the string that is inputted
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
    return jsonify(
        input=message,
        output=True
    )

#Endpoint returns factorial for integer that is inputted. If integer is not positive, an error message will be displayed
@app.route('/factorial/<string:userInput>')
def factorialfunction(userInput):
    userInput=int(userInput)
    if userInput<0:
        return jsonify(
            input=userInput,
            output="Error: You did not enter a positive integer")
    else:
        return jsonify(
        input=userInput,
        output=math.factorial(userInput)
    )

#An array of integers with all Fibonacci numbers less than or equal to the input  will be outputted. If the integer is not positive, an error message will be displayed
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

#A boolean value will be returned depending on whether the input is a prime number. If the input is invalid, an error message will be displayed
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

# This check will only run the code if you run it from the terminal, not if it is imported
if __name__ == '__main__':
    # Set the debug = true
    app.debug = True
    # Run the app
    app.run('0.0.0.0')
