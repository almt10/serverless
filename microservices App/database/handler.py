import requests
import json
import random
import os
from urllib.parse import parse_qs

def handle(req):

    dirname = os.path.dirname(__file__)
    page = os.path.join(dirname, 'json', 'questions.json')

    respuestas = []
    numRespuestas = 2
    Resp_seleccionadas = []

    with(open(page,'r')) as file:
        result = json.load(file)

    for i in range(0,numRespuestas):
        num = random.randint(1,result["number"])
        while num in Resp_seleccionadas:
            num = random.randint(1,result["number"])
        
        for j in result["questions"]:
            if num == int(j["Id"]):
                respuestas.append(j)
                Resp_seleccionadas.append(num)
        
    return json.dumps(respuestas)