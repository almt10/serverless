import requests
import json
import random
import os
from urllib.parse import parse_qs

def handle(req):

    #r = requests.get("http://34.90.72.168/users.json")
    #result = r.json()

    dirname = os.path.dirname(__file__)
    page = os.path.join(dirname, 'json', 'users.json')

    with(open(page,'r')) as file:
        result = json.load(file)

    text = req.split("-")
    Id = text[0]
    if len(text)>=2:
        Passw = text[1]
    else:
        Passw = " "

    for user in result["people"]:
        if  Id == user["userId"] and Passw == user["passwd"]:
            message = "Usuario Registrado como "+user["role"]+".\n\n" + "Bienvenido, %s" % user["name"]
            resp = user["role"]
            break
        else:
            message = "Usuario NO registrado."
            resp = "NO"

    return resp
   
    
 