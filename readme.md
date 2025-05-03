# ecobici-data-science-workflow

## Descripción general
Este proyecto analiza los registros de viajes del sistema ECOBICI de la Ciudad de México utilizando un flujo de trabajo basado en la metodología **CRISP-DM**. Incluye dos procesos **ETL** que permiten extraer, transformar y cargar los datos en una base de datos **MongoDB Atlas** para su posterior análisis y modelado.

## Tecnologías
- Python  
- MongoDB Atlas

## Estructura del proyecto
- **etl_historico**: Conjunto de scripts responsables del proceso ETL que transforma registros históricos desde archivos CSV hacia MongoDB Atlas.  
- **etl_station**: Conjunto de scripts que realizan el proceso ETL a partir de la API con informacion de las estaciones de ECOBICI hacia MongoDB Atlas.  
- **Models**: Contiene las clases que representan cada colección almacenada en MongoDB Atlas.

## Modelos de predicción

### Predicción de estaciones de arribo
Se utilizó un modelo **RandomForest**. Las variables consideradas fueron:

- `genero`: Género del usuario por viaje  
- `start_cluster`: Clúster de las estaciones de retiro  
- `stop_cluster`: Clúster de las estaciones de arribo  
- `hora_retiro_sin`: Hora de retiro representada de forma cíclica (seno)  
- `hora_retiro_cos`: Hora de retiro representada de forma cíclica (coseno)

### Pronóstico de cantidad de retiros por día
También se empleó un modelo **RandomForest**. Las variables utilizadas fueron:

- `fecha`: Fecha del retiro  
- `conteo`: Número de retiros registrados en esa fecha

### Dashboard de análisis

<iframe title="EstacionesAtlas" display="flex"
align-items= "center" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMDA1YWJiOWUtMzgxNS00ZWQ2LThkOGMtNjZmNzE4M2I2YWY2IiwidCI6IjVmMjgyOTEwLTE3NmYtNDU5ZC1hYjdkLWI3NDRhYTZlZmMwNyIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>