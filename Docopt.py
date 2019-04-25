#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Use quotations around inputs
usage = """Usage:
        Docopt.py -h
        Docopt.py md5 <input>
        Docopt.py factorial <input>
        Docopt.py fibonacci <input>
        Docopt.py is-prime <input>
        Docopt.py kv-retrieve <input>
        Docopt.py kv-record <input> <value>
        Docopt.py slack-alert <input>
"""

from docopt import docopt
import requests

args = docopt(usage)

if args['md5']==True:
    r = requests.get("http://api.blackard.org:5000/md5/"+ args["<input>"])
    data = r.json()
    print(data['output'])
if args['factorial']==True:
    r = requests.get("http://api.blackard.org:5000/factorial/"+ args["<input>"])
    data = r.json()
    print(data['output'])
if args['fibonacci']==True:
    r = requests.get("http://api.blackard.org:5000/fibonacci/"+ args["<input>"])
    data = r.json()
    print(data['output'])
if args['is-prime']==True:
    r = requests.get("http://api.blackard.org:5000/is-prime/"+ args["<input>"])
    data = r.json()
    print(data['output'])
if args['kv-retrieve']==True:
    r = requests.get("http://api.blackard.org:5000/kv-retrieve/"+ args["<input>"])
    data = r.json()
    print(data['value'])
if args['kv-record']==True:
    r = requests.get("http://api.blackard.org:5000/kv-retrieve/"+ args["<input>"])
    data = r.json()
    if(data['error']=="ID does not exist"):
        r = requests.post(("http://api.blackard.org:5000/kv-record/"+ args["<input>"]),data=args["<value>"])
        data = r.json()
        print(data['output'])
    if(data['output']==True):
        r = requests.put(("http://api.blackard.org:5000/kv-record/"+ args["<input>"]),data=args["<value>"])
        data = r.json()
        print(data['output'])

if args['slack-alert']==True:
    r = requests.get("http://api.blackard.org:5000/slack-alert/"+ args["<input>"])
    data = r.json()
    print(data['output'])
