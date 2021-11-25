
import requests
import json
from datetime import datetime

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
#print (getTime())

def getDate():
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y")
    return current_time
