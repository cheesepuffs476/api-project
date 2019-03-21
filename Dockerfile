FROM python:3.7
WORKDIR /usr/src/app
RUN git clone https://github.com/cheesepuffs476/project4.git
WORKDIR /usr/src/app/project4
RUN pip install -r requirements.txt
CMD python main.py
