import os
import json
import time

def handle(req):
    # Read the path or a default from environment variable
    path = os.getenv("save_path", "/tmp/")
    global Openned

    # generate a name using the current timestamp
    t = "stats"
    file_name = path + t

    initial = {'results':[
                    {'userId': 'Admin', 'points': '20','preg1':' ', 'resp1':' ', 'preg2':' ', 'resp2':' '}],
                'questions':[
                    {'qId': '1', 'points':'6', 'text':'¿Es OpenFAAS serverless?', 'numAnsw':'0', 'respTrue':'0', 'respFalse':'0','respBlanco':'0'},
                    {'qId': '2', 'points':'4', 'text':'¿Cual de las siguientes NO es tecnología Serverless?', 'numAnsw':'0', 'respTrue':'0', 'respFalse':'0','respBlanco':'0'},
                    {'qId': '3', 'points':'4', 'text':'¿Como se llama la solucion de AWS que usa serverless?', 'numAnsw':'0', 'respTrue':'0', 'respFalse':'0','respBlanco':'0'},
                    {'qId': '4', 'points':'6', 'text':'¿Cual NO es una caracteristica de serverless?', 'numAnsw':'0', 'respTrue':'0', 'respFalse':'0','respBlanco':'0'},
                    {'qId': '5', 'points':'5', 'text':'¿Con que se puede utilizar OpenFAAS?', 'numAnsw':'0', 'respTrue':'0', 'respFalse':'0','respBlanco':'0'}

                ]                    
              }

    try:
        with open(file_name, "r") as f:
            result = json.load(f)
            f.close()
            msg = result
    except:
        with open(file_name, "w") as f:
            f.write(json.dumps(initial))
            f.close()
            result = initial
            msg = result

    text = req.split("-")
    Id = text[0]

    if Id == "C":
        content = text[1]
        part = content.split("/")

        try:
            data = {'userId': part[0], 'points':part[1],'preg1':part[2], 'resp1':part[3], 'preg2':part[4], 'resp2':part[5]} 
        except:
            msg ="Error al coger los datos del usuario"

        result["results"].append(data)
        # write a file
        with open(file_name, "w") as f:
            f.write(json.dumps(result))
            f.close()

        msg = result

    elif Id == "R":
        if result == "":
            msg = "problem"    
    else:
        msg = "Opcion no reconocida. Escriba C o R"


    return msg