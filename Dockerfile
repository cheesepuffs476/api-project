FROM python:3.7
WORKDIR /usr/src/app
CMD ["sh", "-c", "rm -rf ./project4 && git clone https://github.com/cheesepuffs476/project4.git && cd ./project4 && pip install -r requirements.txt && python main.py"]
