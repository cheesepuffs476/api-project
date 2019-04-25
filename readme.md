# Flask API - TCMG 476

This is a web API built for TCMG 476. It is self contained in a docker image and will start a flask webserver to return JSON data. The code is remotly hosted at http://api.blackard.org:5000. This is continuously updated through a GitLab pipeline.

### What will the code do?

 - It will calculate the md5 hash of characters (/md5/[input]) 
 - It will return the factorial of an integer (/factorial/[input])
 - It will return the fibonacci sequence below a number (/fibonacci/[input])
 - It will return if a number is prime or not (/is-prime/[input])
 - It will send a message to a slack channel (/slack-alert/[input])
 - It will create(POST)/update(PUT) a record in a redis database (/kv-record/[key])  *inside of the body is the value*
 - It will retrieve(GET) the value from the redis database (/kv-retrieve/[key])

### Continuous Integration/Continuous Delivery

Continuous Integration
- The project code is controlled through GitHub which is mirrored on [GitLab](https://gitlab.com/concon2015/api-project)
- The docker file for the API container is monitored and tested on [Docker Hub](https://cloud.docker.com/u/cheesepuffs476/repository/docker/cheesepuffs476/api-project) on each update.
- Each code commit is ran against a series of [tests](https://github.com/cheesepuffs476/api-project/blob/master/automatedtest.py) through GitLab.

Continuous Delivery
- After each successful test, the code moves to be automatically deployed and a notification goes to the slack channel with the deployment time.


### Instructions for Local Use
  - You can run the docker-compose.yml file to start the API and Redis containers 
     ```sh
    $ git clone https://github.com/cheesepuffs476/api-project.git
    $ cd ./api-project
    $ docker-compose up -d
    ```

### Instructions for Remote Use
 - The project is hosted on a server located at api.blackard.org:5000. All the routes can be used the same as the the local version
 
### CLI Use
 - Use quotations when entering a route and input.
 - Requirements are requests and docopt
    ```sh
    $ pip install requests Docopt
    $ python3 Docopt.py [method] [input] (Value)
    ```

### Challanges
- Creating a ready to distrubute program via the docker image
    - We wanted to build a solution that went in line with the easiest user experience and take one command to run. This meant that we had to create the docker file in a way that it would completly take care of setting up the enviorment and downloading the latest code.
- Getting the latest code updates
    - When creating the docker file and setting it up to clone the git repo it would only download the repo at the time of the build. This meant that when the container was stopped and restarted it would not pull the latest code. This was solved by using the CMD function in the docker file to clone the repo and try and install requirements on every startup.
- Handling errors in the program
    - We did our best to handle the errors in the code. This came from picking out scenarios that we knew would not work with our functions and make these checks go in the beginning of each function.
- Standardize the output of the program
    - For this we used jsonify from the flask library. This allowed us to have consistent output from each function which could easily be parsed by another program to have another program easily communicate with this API.
- Testing code commits
    - A robust solution had to be created that would handle each test case and could be used to quickly identify if a commit was ready to be pushed without breaking current functionality. Also a efficient system had to be made so tests could easily be modified and created rather than clunky, hardcoded solutions.
- Continuous Integration/Continuous Delivery
    - GitLab was chosen as the CI/CD platform largly due to the free, web based nature of the tool along with resources surrounding the usage. This allowed a multiple stage pipline to be created which would allow code commits to be tested and pushed to production under a minute.
