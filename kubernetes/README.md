## Principales pasos

1. Inicializamos el cluster en el nodo master como superusuario:
    - kubeadm init
      
    Pudiendo añadir determinadas opciones de configuración, como el CIDR de la subred que
    utilizan los nodos del cluster para comunicarse, entre otras.
   
    La salida de este comando nos proporciona información importante sobre el cluster que acabamos de crear:
      - Las instrucciones que hay que seguir en la máquina que funciona como master y donde hemos ejecutado el 
    comando del punto 1 para que cualquier usuario sin privilegios de superusuario pueda acceder al cluster 
    mediante el comando kubectl. 
      - También encontramos información sobre la necesidad de instalar un pod de 
    red en el cluster.
      - Los comandos que es necesario ejecutar en el terminal de los nodes para unirse al cluster.
      
2. El siguiente paso a seguir será, simplemente, ir ejecutando sucesivamente los comandos que
van a permitir que el resto de usuarios que accedan al master puedan utilizar el comando
kubectl para interaccionar con el cluster.

3. Seguidamente, es necesario instalar un pod de red. Sin embargo, de todos los pods disponibles, el que 
proporciona una implementación sencilla pero totalmente válida para una comunicación simple entre pods es *_Weave Net_*.

4. El siguiente paso a llevar a cabo es la unión de los diferentes nodes al cluster, con la información 
que sale del comando del paso 1.

5. En este punto, ya podemos volver al terminal del master y ejecutar alguna de las funcionalidades del comando kubectl
para interaccionar con el cluster:
      - kubectl get nodes -o wide
      
      
## Más información
En la página oficial de Kubernetes https://kubernetes.io/es/docs/tasks/tools/install-kubectl/
