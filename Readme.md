<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

En este repositorio encontrarás el primer proyecto individual Henry que consiste de 3 partes principales:

1.- La realización de ETL, DEA y el Modelo de recomendación de películas.

2.- FASTAPI.

3.-Deployment del proyecto.

<hr>  

# <h1 align=center> **PLANTEAMIENTO DE PROBLEMA**

## 1.1.- ETL

Realizar la limpieza de los datos de los siguientes csv: **`movies_dataset`** y **`credits`** ubicados en la carpeta **`PI_MLOps`** la cual incluye:

+ Desanidar los datos de las columnas  **`belongs_to_collection`**, **`production_companies`** , etc.

+ Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
  
+ Los valores nulos del campo **`release date`** deben eliminarse.

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.

+ Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.

+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`poster_path`** y **`homepage`**.

+ Unir los datasets: **`movies_dataset`** y **`credits`**

## 1.2.- Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA)

Realizar una análisis exploratorio de los datos una vez limpios, es decir, investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías, analizar la existencia de algún patrón interesante que valga la pena explorar en un análisis posterior. Incluir en el análisis las nubes de palabras para las palabras son más frecuentes en los títulos,

## 1.3.- Modelo de recomendación de películas.

Armar un sistema de recomendación de películas. Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse:


+ def **recomendacion( *`titulo`* )**:
    Se ingresa el nombre de una película y te recomienda las similares en una lista de 5 valores.

## 2.- Desarrollo FASTAPI

Disponibilizar los datos de la empresa usando el framework ***FastAPI*** mediante la creación de las siguientes funciones:

+ def **peliculas_idioma( *`Idioma`: str* )**:
    Se ingresa un idioma (como están escritos en el dataset, no hay que traducirlos!). Debe devolver la cantidad de películas producidas en ese idioma.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` cantidad de películas fueron estrenadas en `idioma`*
         

+ def **peliculas_duracion( *`Pelicula`: str* )**:
    Se ingresa una pelicula. Debe devolver la duracion y el año.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *`X` . Duración: `x`. Año: `xx`*

+ def **franquicia( *`Franquicia`: str* )**:
    Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La franquicia `X` posee `X` peliculas, una ganancia total de `x` y una ganancia promedio de `xx`*

+ def **peliculas_pais( *`Pais`: str* )**:
    Se ingresa un país (como están escritos en el dataset, no hay que traducirlos!), retornando la cantidad de peliculas producidas en el mismo.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *Se produjeron `X` películas en el país `X`*

+ def **productoras_exitosas( *`Productora`: str* )**:
    Se ingresa la productora, entregandote el revunue total y la cantidad de peliculas que realizo. 
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ejemplo de retorno: *La productora `X` ha tenido un revenue de `x`*

+ def **get_director( *`nombre_director`* )**:
    Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma, en formato lista.


##  3.- Deployment del proyecto 

Utilizar un servicio que permita utilizar la API desde la web, por ejemplo: **`Render`** o **`Railway`**


## Extras

El video NO DEBE durar mas de ***7 minutos*** y DEBE mostrar las consultas requeridas en funcionamiento desde la API y una breve explicacion del modelo utilizado para el sistema de recomendacion. En caso de que te sobre tiempo luego de grabarlo, puedes mostrar explicar tu EDA, ETL e incluso cómo desarrollaste la API. Entregar el link de acceso al video el cual puede alojarse en YouTube, Drive o cualquier plataforma de almacenamiento.


## <h1 align=center> Desarrollo 

***1.1.- ETL***

Se inicia con la limpieza de los datos, la cual se encuentra ubicada en el archivo  **`Limpieza_de_datos_2.ipynb`** del repositorio. 
Se utilizan los csv  **`movies_dataset`** y **`credits`** ubicados en la carpeta **`PI_MLOps`**
Se realizan todos los puntos mencionados en el ***planetamiento del problema*** a excepción del desanidado de columnas, ya que al iniciar con la eliminación de las columnas y valores nulos implica trabajar con menos datos, lo que simplifica el proceso. 

Una vez ya "limpios" los 2  dataframes: **`data_movies`** y **`credits`**, se convierte la columna id del dataframe **`data_movies`** de objeto a entero para poder realizar el merge a través de dicha columna. Creando así el nuevo dataframe titulado **`data_movies_credits`**.Se verifica que no haya valores repetidos en nuestro nuevo dataframe y de ser así se eliminan. 

Antes de realizar el desanidado de las columnas  **`belongs_to_collection`**, **`production_companies`**,**`genres`**,**`production_countries`**,**`spoken_languages`**,**`cast`** y **`crew`** es importante verificar qué tipo de dato contienen para saber qué función utilizar. El resultado arrojado indica que a pesar de que tienen una estructura similar a una lista de diccionarios , ejemplo: [{}, {}. {}], los datos almancenados en dichas columnas son de tipo string. Por lo que se propone utilizar la función literal_eval para la transformación de los mismos. Cabe recalcar que no se han eliminado todos los datos np.nan de nuestro dataframe, por lo que para poder utilizar "literal_eval" se crea la función "convert_to_dicc" la cual excluye los valores nulos que se tengan en cada columna. 

Una vez aplicada la función a cada una de las columnas anidadas , los datos resultantes para cada columna son:
+ data_movies_credits['genres']= lista de diccionario [{}, {}. {}]
+ data_movies_credits['belongs_to_collection']= #diccionario {}
+ data_movies_credits['production_companies']= #lista de diccionario [{}, {}. {}]
+ data_movies_credits['production_countries']= #lista de diccionario [{}, {}. {}]
+ data_movies_credits['spoken_languages']= #lista de diccionario [{}, {}. {}]
+ data_movies_credits['cast']= #lista de diccionario [{}, {}. {}]
+ data_movies_credits['crew']= #lista de diccionario [{}, {}. {}]

Aún no terminamos desanidar la información. 

+ Para las columnas **`production_companies`**, **`genres`**, **`production_countries`**, **`spoken_languages`**, **`cast`**, la key más importante y que nos interesa es la de *`"name"`* por lo que se crea una función que regresa en forma de lista los campos en donde la key= 'name'. 

+ Para la columna **`crew`**, la key más importante y que nos interesa es la de *`"director"`* por lo que se crea una función que regresa en forma de lista los campos en donde la key= 'director'. 

+ Para la columna **`belongs_to_collection`**, la key más importante y que nos interesa es la de *`"collection"`* por lo que se crea una función que regresa en forma de lista los campos en donde la key= 'collection'. 

Por último se verifica que efectivamente el tipo de dato sea lista en todas las columnas desanidadas y se exporta el archivo en formato csv titulado  **`'data_movies_credits_datos_filtrados'`**, esto para poder hacer el análisis exploratorio de los datos. 



***1.2.- EDA***

Se inicia con el análisis exploratorio de los datos, el cual se encuentra ubicado en el archivo  **`EDA.ipynb`** del repositorio. El csv utilizado es  **`'data_movies_credits_datos_filtrados'`**


+ Para realizar la investigación sobre las relaciones entre las variables de los datasets se crea una matriz de correlación para las columnas **`budget`**, **`popularity`**, **`revenue`**, **`vote_average`**, **`vote_count`**, **`return`**, **`release_year`**. Los resultados obtenidos se pueden encontrar en el apartado ***Conclusiones***	

+ Se revisa si existen outliers en **`popularity`**, es decir en el Puntaje de las Películas. 

+ Se grafica el número de películas por categoría, país, 'estatus', idioma, año.  También se grafica el Top 10 de colecciones con mayor número de películas

+ Por último se crea nubes de palabras para las palabras son más frecuentes en los títulos. 



***1.3.- Modelo de recomendación de películas.***

Se inicia con el Modelo de recomendación de películas, el cual se encuentra ubicado en el archivo  **`Limpieza_de_datos_2.ipynb`** del repositorio. 

Se realiza la elección de columnas y cambio de nombre como se muestra a continuación: 
+ data_modelo=data_movies_credits[['id','title','original_language','overview','genres','cast','crew']]
+ data_modelo.columns = ['id_pelicula', 'titulo','idioma_original', 'sinopsis', 'genero', 'actores', 'director']

Lo que queremos lograr para el modelo de recomendación es crear una nueva columna que contenga toda la información que contienen todas las columnas (**`id_pelicula`**, **`titulo`**, **`idioma_original`**, **`sinopsis`**, **`genero`**, **`actores`**, **`director`**) en forma de string. Para ello lo primero que se hace es convertir la columna sinopsis en una lista.

Para la columna **`actores`** y **`director`** tenemos varios nombres que coinciden sin embargo su apellido no. Esto puede afectar nuestro algoritmo por lo que se eliminan los espacios entre Nomnre-Apellido de dichas columnas es decir, si la fila es [Tom Hanks, Tim Allen, Don Rickles], el resultado sería [TomHanks, TimAllen, DonRickles]

Una vez hecho esto, se busca tener todos los datos de todas las columnas en una sola. Ya creada la columna con toda la información (llamada **`tags`**) se procede a eliminar el resto de las columnas puesto que sería tener información repetida. Se eliminan las mayúsculas. Por lo tanto nuestro dataframe llamado **`data_tags`** estaría conformado por las columnas: **`título`**, **`id`** y **`tags`** 

Si nos enfocamos en la columna **`tags`** podemos ver que hay varias palabras que tienen la misma raíz, por lo que podemos utilizar **`nltk.stem.porter`** para pasar de esto: ['loved', 'loving', 'love'] a:  ['love','love','love']

Procedemos a crear un vector para cada dato de **`tags`**, es decir, para cada película. Para ésto se utiliza CountVectorizer. 
En este caso, especificamos las 2500 palabras más frecuentes que existen es esta columna y también que las palabras que deben ser excluidas del análisis , es decir, "las palabras parada" (por ejemplo: "el", "es", "y", "un", etc.) están en 'english'. CountVectorizer utilizará una lista predeterminada de "palabras de parada" en inglés. Una vez creado el objeto se  aplica el CountVectorizer a la columna **`tags`**
Como resultado tendremos una matriz de tamaño: (Número de películas que tenemos en nuestro dataframe x las 2500 palabras que especificamos)

Lo que sigue es saber qué tan similar es un vector de otro , esto es, medir la distancia entre ellos para deducir la similitud. Entre más distancia entre dos vectores menor similitud.Para 1 vector (1 película) se calculan 44936  ángulos ,es decir, una matriz de  (# total de películas X # total de películas)

Ya que tenemos la matriz de similaridad, se crea la función de recomendación para arrojar 5 recomendaciones por película.
Esta función a grandes rasgos busca el índice de la película que queremos en **`data_tags`** y nos devuelve el índice de las películas que tienen mayor similutud de la **`matriz de similitaridad`** Con esos índices bucar los títulos de las películas los cuales son devueltos en forma de lista. 

Aplicamos la función de recomendación para cada una de las películas que tenemos, es decir, a toda la columna **`titulo`** del dataframe **`data_tags`** para poder crear un nuevo dataframe, usarlo en el deploy y facilitarlo. Este nuevo dataframe llamado **`data_recomendaciones_final`** será utilizado en FASTAPI. NOTA: Recordar que para poder aplicar la función a **`data_tags`**, este dataframe debe de tener los mismos índices que la matriz de similaridad. Puede llegar a saltar error si dropeas filas que contengan np.nan y no reseteas el índice data_tags.reset_index(drop=True, inplace=True)



***2.- FastApi***

Se inicia con el desarrollo de las funciones requeridas en el apartado ***planetamiento del problema*** para FASTAPI , el cual se encuentra ubicado en el archivo  **`main.py`** del repositorio. 

Se realizan las instalaciones necesarias para poder utilizar FastApi en Python, así como el uso de un entorno virtual. 
+ El comando para iniciar el entorno virtual es: python -m uvicorn main:app --reload
+ El comando para finalizar el entorno virtual es: Control + C

Se importan las librerías necesarias para el correcto funcionamiento de las funciones. 

Los dataframes utilizados para las funciones son: **`data_recomendaciones_final`** para el modelo de recomendación y 
**`data_movies_credits`** para el resto de las funciones. 

Se crea una instancia de FastAPI  ***app = FastAPI()***

Antes de cada función se escribe @app.get(""). 

***3.- Deployment***


## <h1 align=center> Conclusiones EDA

Después de realizar el análisis exploratorio de los datos, se llegan a las siguientes conclusiones:

Las variables que presentan una relación superior a la media:
+ budget-revenue (0.768738)
+ popularity -vote_count(0.559937),revenue(0.506183)
+ revenue- vote_count(0.812013)

Puntaje de las películas contiene outliers, sin embargo como esta columna no se consideró para el modelo se ignora.

El país con más películas es Estados Unidos, seguido por valores np.nan

La categoría con mayor número de películas es Drama, Comedia, seguido de Thriller. 

Al graficar el número de películas por Estatus se detectó que el dataframe contenía películas : Released, Rumored, PostProduction, InProduction, Planned y Canceled por lo que se eliminaron todas las películas diferentes a Released.  

Existen mayor número de películas en idioma inglés. 

El número de películas por año fue aumentando exponencialmente. 

Según google la primer película que se filmó fue en 1895, sin embargo, en el dataframe se encontraron películas en años: 1887, 1878, 1874, 1883. Por lo que se eliminaron de los registros. 

La colección con mayor número de películas fue 'The Bowery Boys' seguida de 'Totó Collection'


