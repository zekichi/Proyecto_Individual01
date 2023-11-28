from fastapi import FastAPI
from fastapi import HTTPException
from funciones import PlaytimeGenre
from funciones import UserForGenre
from funciones import UsersRecommend
from funciones import UserWorstDeveloper
from funciones import sentiment_analysis
from funciones import recomendacion_juego

app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return "Hola"

@app.get('/PlayTimeGenre/{genre}')
async def user(genre : str):
    try: 
        response =  PlaytimeGenre(genre)
        return response
    except Exception as e:
        return{'error': str(e)}
    


#-------- funcion 1 -------    
@app.get('/UserForGenre/{genre}')

async def user(genre: str):
    try:
        response = UserForGenre(genre)
        return response
    except Exception as e:
        return{'error': str(e)}
    

#------ funcion 2 ------
@app.get('/UserRecommend/{año}')
async def user(year: str):
    try:
        response = UsersRecommend(year)
        return response
    except Exception as e:
        #raise HTTPException(status_code=500, detail=str(e))
        return {'error': str(e)}
    

#------ funcion 3 ------
@app.get('/UserWorstDeveloper/{año}')
async def user(year: str):
    try:
        response = UserWorstDeveloper(year)
        return response
    except Exception as e:
        return {'error': str(e)}
    
#------ funcion 4 ------
@app.get('/sentiment_analysis/{developer}')
async def user(developer: str):
    try:
        response = sentiment_analysis(developer)
        return response
    except Exception as e:
        return {"error": str(e)}
    

#------ funcion 5 ------    
@app.get('/recomendacion_juego/{id}')
async def user (id: int):
    try:
        response = recomendacion_juego(id)
        return response
    except Exception as e :
        return {'error': str(e)}