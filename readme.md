# Flask API - TCMG 476

This is a web API built for TCMG 476. It is self contained in a docker image and will start a flask webserver to return JSON data.

# What will the code do?

 - It will calculate the md5 hash of characters (/md5/[input]) 
 - It will return the factorial of an integer (/factorial/[input])
 - It will return the fibonacci sequence below a number (/fibonacci/[input])
 - It will return if a number is prime or not (/is-prime/[input])
 - It will send a message to a slack channel (/slack-alert/[input])

# Instructions for Use
  - You can run the file by pulling the docker image. (The line below will run on port 80, delete the container after stopping and run in the background)
 ```sh
$ docker run -d --rm -p 80:5000 cheesepuffs476/project4:latest
```

# Challanges
- Creating a ready to distrubute program via the docker image
    - We wanted to build a solution that went in line with the easiest user experience and take one command to run. This meant that we had to create the docker file in a way that it would completly take care of setting up the enviorment and downloading the latest code.
- Getting the latest code updates
    - When creating the docker file and setting it up to clone the git repo it would only download the repo at the time of the build. This meant that when the container was stopped and restarted it would not pull the latest code. This was solved by using the CMD function in the docker file to clone the repo and try and install requirements on every startup.
- Handling errors in the program
    - We did our best to handle the errors in the code. This came from picking out scenarios that we knew would not work with our functions and make these checks go in the beginning of each function.
- Standardize the output of the program
    - For this we used jsonify from the flask library. This allowed us to have consistent output from each function which could easily be parsed by another program to have another program easily communicate with this API.
