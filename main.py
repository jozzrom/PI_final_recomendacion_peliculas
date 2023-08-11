from fastapi import FastAPI
import pandas as pd
import numpy as np
import ast 

#df=pd.read_csv('data_movies_credits')
df=pd.read_csv('df_2')
df_recomendaciones=pd.read_csv('data_recomendaciones_final')

# Crea una instancia de FastAPI
app = FastAPI()

#1
@app.get("/peliculas_idioma/{idioma}")
def peliculas_idioma(idioma: str):
    y= df[['original_language']].value_counts()
        #la serie la convertimos a dataframe y cambiamos el nombre de las columnas
    y = y.reset_index()
    y.columns = ['original_language', 'count']

    if idioma in y['original_language'].values:
        # Filtrar el DataFrame y obtener la cantidad de películas en el idioma especificado
        cantidad_peliculas = y[y['original_language'] == idioma]['count'].values[0]
        
        return {'idioma':idioma, 'cantidad':int(cantidad_peliculas)}

#2    
@app.get("/peliculas_duracion/{pelicula}")
def peliculas_duracion( pelicula: str ):
    if type(pelicula)== str:
        if pelicula in df['title'].values:
        # Filtrar el DataFrame y obtener la cantidad de películas en el idioma especificado
            duracion = df[df['title'] == pelicula]['runtime'].values[0]
            anio=df[df['title'] == pelicula]['release_year'].values[0]
            return {'pelicula':pelicula, 'duracion':int(duracion), 'anio':int(anio)}

#3        
@app.get("/franquicia/{franquicia}")
def franquicia( franquicia: str ):
    if type(franquicia)== str:
        if franquicia in df['belongs_to_collection'].values:
            y1=df[df['belongs_to_collection']==franquicia]['belongs_to_collection'].values
            cantidad_peliculas=len(y1)
            ganancia_total = sum(df[df['belongs_to_collection']==franquicia]['return'].values)
            promedio = np.mean(df[df['belongs_to_collection']==franquicia]['return'].values)
            return {'franquicia':franquicia, 'cantidad':int(cantidad_peliculas), 
            'ganancia_total':int(ganancia_total), 'ganancia_promedio':int(promedio)}
        
#4
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais: str):
    # Filtrar el DataFrame para obtener las películas producidas en el país especificado
    cantidad_peliculas = df[df['production_countries'].apply(lambda paises: pais in paises)].shape[0]
    
    return {'pais':pais, 'cantidad':int(cantidad_peliculas)}

#5
@app.get("/productoras_exitosas/{productora}")
def productoras_exitosas( productora: str ):
    #Convertimos la columna tipo str a lista
    convert_to_dicc = lambda string_a_dicc: ast.literal_eval(string_a_dicc) if isinstance(string_a_dicc, str) else np.nan
    df['production_companies2'] = df['production_companies'].apply(convert_to_dicc)

    # Variables para almacenar el conteo de películas y el total de revenue
    cantidad_peliculas = 0
    revenue_total = 0
    if type(productora) == str:
        for i in df['production_companies2'].values:
            if productora in i:
                matching_rows = df[df['production_companies2'].apply(lambda x: isinstance(x, list) and productora in x)]
                matching_rows2 = pd.DataFrame(matching_rows)
                cantidad_peliculas = len(matching_rows2)
                revenue_total = matching_rows2['revenue'].sum()
                break  # Salir del bucle una vez que se encuentra la coincidencia

        return {'productora':productora, 'revenue_total': int(revenue_total),'cantidad':int(cantidad_peliculas)} 

#6
@app.get("/get_director/{nombre_director}")
def get_director(nombre_director):
    #Convertimos la columna tipo str a lista
    convert_to_dicc = lambda string_a_dicc: ast.literal_eval(string_a_dicc) if isinstance(string_a_dicc, str) else np.nan
    df['crew2'] = df['crew'].apply(convert_to_dicc)

    # Variables para almacenar el conteo de películas y el total de revenue
    retorno_total_director=[]
    peliculas=[]
    anio=[]
    retorno_pelicula=[]
    budget_pelicula=[]
    revenue_pelicula=[]
    if type(nombre_director) == str:
        for i in df['crew2'].values:
            if type(i) == list and nombre_director in i:
                matching_rows = df[df['crew2'].apply(lambda x: isinstance(x, list) and nombre_director in x)]
                matching_rows2 = pd.DataFrame(matching_rows)
                matching_rows2=matching_rows2[['title','release_year','return','revenue','budget','crew2']]
                retorno_total_director.append(matching_rows2['return'].sum())
                for i in matching_rows2['title']:
                    peliculas.append(i)
                for i in matching_rows2['release_year']:
                    anio.append(i)
                for i in matching_rows2['return']:
                    retorno_pelicula.append(i)
                for i in matching_rows2['budget']:
                    budget_pelicula.append(i)
                for i in matching_rows2['revenue']:
                    revenue_pelicula.append(i)

                break
        # Crear un diccionario para almacenar la información
        return {'director':nombre_director, 'retorno_total_director':retorno_total_director, 
        'peliculas':peliculas, 'anio':anio, 'retorno_pelicula':retorno_pelicula, 
        'budget_pelicula':budget_pelicula, 'revenue_pelicula':revenue_pelicula}

#ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo): 
    convert_to_dicc_2 = lambda string_a_dicc: ast.literal_eval(string_a_dicc) if isinstance(string_a_dicc, str) else np.nan
    df_recomendaciones['recomendaciones2'] = df_recomendaciones['recomendaciones'].apply(convert_to_dicc_2)
    if titulo in df_recomendaciones['titulo'].values:
        mi_string = df_recomendaciones[df_recomendaciones['titulo'] == titulo]['recomendaciones2'].iloc[0]
        return {'lista recomendada': mi_string}