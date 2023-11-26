import pandas as pd
import fastapi
from fastapi import FastAPI
import pyarrow.parquet as pq
import pickle
from collections import Counter


#carga de dataFrames
steam_games = pd.read_parquet('./steam_games.parquet')
steam_reviews = pd.read_parquet('./steam_reviews.parquet')
steam_items = pd.read_parquet('./steam_items.parquet')
df = pd.read_parquet('./modelado.parquet')

#-------- funcion 1 --------

def PlaytimeGenre(genre: str):
    
    if not isinstance(genre, str):
        return{'El parametro no es un valor del tipo cadena (str)'}
    
    df_merge = pd.merge(steam_games, steam_items, left_on='item_id', right_on='item_id', how='inner')

    if df_merge.empty:
        return {'No existen parametros para devolver para dicho genero {}'.format(genre)}

    mas_horas = df_merge.groupby('año')['playtime_forever'].sum()
    

    mas_horas_max = mas_horas.idxmax()

    return {"Mas horas jugadas por año de lanzamiento {}: {}".format(genre, int(mas_horas_max))}


#-------- funcion 2 --------

def UserForGenre(genre: str):

    if not isinstance(genre, str):
        return{'El parámetro no es un valor del tipo cadena (str)'}
    
    df_merge = pd.merge(steam_games, steam_items, left_on='item_id', right_on='item_id')

    if df_merge.empty:
        return{'No existen parametros para devolver para dicho genero {}'.format(genre)}
    
    usuario_mas_horas = df_merge.groupby('user_id')['playtime_forever'].sum().idxmax()

    usuario_mas_horas_max = df_merge[df_merge['user_id'] == usuario_mas_horas]

    horas_año = usuario_mas_horas_max.groupby('año')['playtime_forever'].sum().reset_index()

    return{
        'El Usuario con mas horas jugadas {}'.format(genre) : usuario_mas_horas,
        'Total de horas' : [{'Año': int(year), 'horas': int(time)} for year, time in zip(horas_año['año'], (horas_año['playtime_forever'])/60)]
    }


#-------- funcion 3 --------
def UsersRecommend(year: int):
    try:
        year = int(year)

        
        reviews = steam_reviews[(steam_reviews['año'] == year) & (steam_reviews['recommend']) & (steam_reviews['sentiment_analysis'] == 2)]


        reviews['item_id'] = reviews['item_id'].astype(int)
        steam_games['item_id'] = steam_games['item_id'].astype(int)
        df_merge = pd.merge(reviews, steam_games, left_on='item_id', right_on='item_id', how='inner')

        game_recommend = df_merge['app_name'].value_counts()

        top = game_recommend.head(3)

        list = [{"Puesto {}".format(i + 1): game} for i, game in enumerate(top.index)]

        return list
    except ValueError:
        return {"Error": "Por favor, ingrese un año válido como entero"}

#-------- funcion 4 --------
def UserWorstDeveloper(year: int):
    try:
        year = int(year)


        
        reviews = steam_reviews[(steam_reviews['año'] == year) & (steam_reviews['recommend']) & (steam_reviews['sentiment_analysis'] == 0)]

        reviews['item_id'] = reviews['item_id'].astype(int)
        steam_games['item_id'] = steam_games['item_id'].astype(int)
        merged_df = pd.merge(reviews, steam_games, left_on='item_id', right_on='item_id', how='inner')

        developer_counts = merged_df['developer'].value_counts()

        top = developer_counts.head(3)

        list = [{"Puesto {}".format(i + 1): developer} for i, developer in enumerate(top.index)]

        return list
   
    except ValueError:

        return {"Error": "Por favor, ingrese un año válido como entero"}
    

#-------- funcion 4 --------
def sentiment_analysis(developer: str):

    if not isinstance(developer, str):
        return{'El parámetro no es un valor del tipo cadena (str)'}
    
    reviews = steam_reviews[steam_reviews['item_id'].isin(steam_games[steam_games['developer'] == developer]['item_id'])]
    
    sentiment = reviews['sentiment_analysis'].astype(int).tolist()
    contador = Counter(sentiment)

    response = {developer: {'Negativo': contador.get(0,0),
                            'Neutral': contador.get(1,0),
                            'Positivo': contador.get(2, 0)}}
    
    return response

#-------- funcion 5 --------

