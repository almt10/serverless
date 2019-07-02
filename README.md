# Plataforma Serverless y Aplicación basada en microservicios
Diseño y despliegue de una aplicación basada en microservicios sobre una plataforma Serverless de código abierto. 

Este estudio se corresponde con el *Trabajo Fin de Máster (MUIT) de Alberto Marugán Torres en la Universidad Politécnica de Madrid (UPM).*

## Principales pasos
Los principales puntos a seguir para conseguir desplegar esta solución son:
  1. Configurar un orquestador sobre un clúster de máquinas virtuales
  2. Desplegar la plataforma Serverless
  3. Crear y subir a la plataforma la aplicación basada en microservicios
  4. Ejecutar la aplicación para comprobar que todo funciona correctamente
  5. Testear y monitorizar las principales características de la plataforma
 
## Confiruar un orquestador
En nuestro caso, hemos optado por desplegar la solución utilizando tanto Docker Swarm como Kubernetes, con el objeto de analizar ambos orquestadores.

La información del despliegue de ambos se encuentra en las carpetas *Kubernetes y Docker Swarm* del repositorio.

Como comentario general, Docker Swarm es más fácil de desplegar, requeriendo incluso un menor número de máquinas virtuales. Por lo tanto, en nuestro caso, lo hemos utilizado para un entorno de desarrollo y pruebas. 

Por el otro lado, Kubernetes es más complejo y requiere una mayor comprensión de conceptos y configuraciones. Es por ello que, en nuestro despliegue, ha sido utilizado en el entorno de producción o entorno final.

## Desplegar la Plataforma Serverless
En este punto también se ha optado por probar dos tipos de plataformas con el mismo fin, comparar ambas soluciones para quedarnos con la que más ventajas tiene.

Desde mi punto de vista, la plataforma **OpenFaaS** proporciona un mayor número de ventajas que *Kubeless*, por lo que se ha optado por utilizar esta plataforma como solución final.

La información de cómo desplegar cada una de ellas se encuentra en las carpetas *OpenFaas y Kubeless* de este repositorio.

## Diseño de una aplicación basada en microservicios
La aplicación creada tiene la funcionalidad básica de permitir a un grupo de usuarios realizar un *Test* para que el administrador acceda a las estadísticas del cuestionario.

Para ello, se han creado 4 microservicios principales. Estos microservicios y la lógica que siguen es posible encontrarlos en la carpeta *microservices App* del presente respositorio.

## Ejecución de microservicios
Simplemente es necesario seguir las reglas o pasos para ejecución de funciones que se mencionan en *OpenFaaS*, que son las reglas comunes para la ejecución de cualquier función en la plataforma mencionada.

## Testeo y monitorización
Para llevar a cabo la monitorización de las principales características, se han utilizado las herramientas **Prometheus y Grafana** que recomienda la plataforma *OpenFaaS* en su documentación oficial.

Un ejemplo de la solución de código abierto para monitorización, *Grafana*:

<img src="https://static.wixstatic.com/media/36ad7e_fc6109f2dfcd477592cfd03e9ee5a521~mv2.gif" />
