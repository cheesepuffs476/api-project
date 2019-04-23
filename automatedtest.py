import requests

# api-endpoint
URL = "http://api.blackard.org:5000"
exitcode = 0
#test all routes using POST method   [route,output,data]
testpost = [ ['/kv-record/autotestvalue',True,'autotestvalue']   ]
for item in testpost:
  url = URL + item[0]
  r = requests.post(url,data=item[2])
  data = r.json()
  if data['output']!=item[1] and data['error']!='Value already exists':
    print("Failed test " + item[0] + " by returning " + str(data['output']))
    exitcode = 1

#test all routes using PUT method [route,output,data]
testput = [ ['/kv-record/autotestvalue',True,'autotestvalueupdated']   ]
for item in testput:
  url = URL + item[0]
  r = requests.put(url,data=item[2])
  data = r.json()
  if data['output']!=item[1]:
    print("Failed test " + item[0] + " by returning " + str(data['output']))
    exitcode = 1

#test all routes using GET method     [route,output]
testget = [  ['/md5/test','098f6bcd4621d373cade4e832627b4f6']  , ['/fibonacci/15',[1, 1, 2, 3, 5, 8, 13]] , ['/is-prime/15',False],['/is-prime/13',True]   ]
for item in testget:
  url = URL + item[0]
  r = requests.get(url)
  data = r.json()
  if data['output']!=item[1]:
    print("Failed test " + item[0] + " by returning " + str(data['output']))
    exitcode = 1


#return exit code
exit(exitcode)

#echo $? to test the exit code on linux based systems
