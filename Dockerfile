FROM python:3.7
WORKDIR /usr/src/app
CMD chmod +x /usr/src/app/main.py
CMD ./test.sh
