import random
import time
import os
import requests
from pymongo import MongoClient

PASS=os.environ['pass']
cluster1=MongoClient(f'mongodb+srv://progr-py:{PASS}@cluster0.macl44c.mongodb.net/?retryWrites=true')
db1=cluster1["telegram"]
collection1 = db1["athkar"]


cluster=MongoClient(f'mongodb+srv://progr-py:{PASS}@cluster0.macl44c.mongodb.net/?retryWrites=true')
db=cluster["telegram"]
collection = db["athkar-users"]
TOKEN = os.environ['token']



def rand():
    a = collection1.find()
    i = -1
    for a in a:
        i = i + 1
    return random.randint(0, i)
def getTheker():
    a= collection1.find({'_id': rand()})
    for a in a:
        return a['t']
def ru():

  
        a = collection.find()
        for a in a:
            if(a['status']=='on'):
                url = F"https://api.telegram.org/bot{TOKEN}/sendMessage"


                payload = {
                    "text": getTheker(),
                    "chat_id": a['_id']
                }
                headers = {
                    "Content-Type": "application/json"
                }

                response = requests.post(url, json=payload, headers=headers)

while True:
        try:
                ru()
        except:
                time.sleep(100)
        time.sleep(7000)
