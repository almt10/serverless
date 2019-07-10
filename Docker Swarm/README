## Principales pasos

1. Es necesario contar con al menos 2 máquinas virtuales que cuenten con Docker Engine.

2. Una vez instalado y comprobado que podemos utilizar el comando “docker”, es momento de crear el
swarm o cluster de nodos:

    2. 1. Para ello, en el terminal de la máquina que queramos utilizar como master ejecutamos:
            docker swarm init
        
        La salida de este comando nos devuelve directamente el comando que hay que ejecutar en el
        terminal de la o las máquinas que actuarán como workers. 
        
        Básicamente, la información que obtenemos es un identificador o “token” que es necesario pasar 
        al orquestador de docker swarm para que permita la entrada en el cluster o swarm al que queremos 
        unirnos. Esta información puede variar en función de si queremos que la máquina se añada como
        master o como worker.

    2. 2. Además del token necesario, también es necesario pasar como parámetro la dirección IP del
        master y el puerto en el que escucha las peticiones hacia el swarm. Como ejemplo:
            docker swarm join --token SWMTKN-1-
            1x5dk8l84579j3hu9d4k9lut7gkg69p91gqmke0uf8tu23evmi-bepqzyb4axlhzlc8ao1o7129s
            192.168.213.137:2377
