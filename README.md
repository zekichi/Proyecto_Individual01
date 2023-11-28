# Proyecto_Individual01 MLOps

## Descripción 

Este proyecto se centra en el desarrollo de una API para obtener información detallada sobre juegos de Steam, usuarios y recomendaciones. Utilizando conjuntos de datos específicos de Steam, implementé endpoints que ofrecen datos relevantes sobre juegos, reseñas de usuarios y elementos del juego. La API, creada con Python y FastAPI, está optimizada para respuestas rápidas y eficientes. Además, incorporé un modelo de recomendación de juegos mediante machine learning. El proceso ETL garantiza la limpieza y eficiencia en el manejo de grandes conjuntos de datos, y el servicio web se encuentra actualmente desplegado en Render, facilitando el acceso a la información sobre la plataforma Steam.


+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit?usp=drive_link): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
<br/>


##ETL

Se recibieron 3 archivos .json, de los cuales se extrajeron los datos necesarios. Todo este proceso se hizo en un ETL principal donde se trabajó los 3 conjuntos.
Se realizó una limpieza de datos de estos 3 archivos, eliminando valores nulos y cambiando el tipo de datos de algunas columnas, para así ya lograr tener unos archivos .parquet con los cuales se iba a seguir a la etapa del Analisi exploratorio de los datos


##API

Se hizo un desarrollo de una API, por medio de FastAPI, donde deployamos las funciones que se pedían. Estos son 5 endpoints los cuales son:
  + PlayTimeGenre : este devuelve el año con más horas jugadas para un genero dado por el usuario
  + UserForGenre : Devuelve el usuario que tiene más horas jugadas para un genero dado, junto a una lista que muestra las horas que jugo por año
  + UserRecommend : Devuelve un top 3 de los juegos que se recomiendan mas según el año dado por el usuario
  + UserWorstDeveloper : Devuelve un top 3 de los desarrolladores con menor recomendaciones para el año dado por el usuario
  + sentiment_analysis : Devuelve un diccionario con la cantidad de reseñas recibidas segun la empresa desarrolladora dada por el usuario

Luego de que funciones esto se hizo el deployment de la API en Render

##EDA

En esta etapa, se realizo un analisis para acondicionar los datos para futuras predicciones, haciendo busqueda de valores atipicos u outliers dentro de nuestros DataFrames. Este proceso tambien se realizó dento de un solo archivo principal, donde se hizo el analisis a los 3 DataFrames. Al hacer este analisis se comprendió mejor las relaciones, patrones e irregularidades.

##Modelo de ML

Se creo un modelo de Machine Learning para la creación de un endpoint más, el cual es un sistema de recomendación donde según un id dado por el usuario se recibe una lista con 5 juegos recomendado similares al ingresado

##Video Explicativo

Se creo un Video donde se explica el proyecto, este se encuentra en Youtube y este es el link al mismo:


#Creador
Nombre: Ezequiel Quintana
Repositorio: https://github.com/zekichi/Proyecto_Individual01.git
Mail : equintana779@gmail.com
