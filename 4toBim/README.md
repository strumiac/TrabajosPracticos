<img src="https://github.com/FIUBA-Posgrado-Inteligencia-Artificial/procesamiento_lenguaje_natural/raw/main/logoFIUBA.jpg" width="500" align="center">

# Procesamiento del Lenguaje natural
Este repositorio contiene la resolución (notebooks) a los desafíos semanales planteados en la asignatura NLP perteneciente a la Carrera de Especialización en Inteligencia Artificial (CEIA - FIUBA).

## Contenido

### [Desafío 1](NLP/1a_word2vec.ipynb) 
<img src="https://github.com/strumiac/TrabajosPracticos/blob/main/4toBim/fig/1-vectorizacion.png" width="80" align="left">
<aside>Se transformó un cierto corpus (array de documentos) en una lista de términos y se armó un vector de términos no repetidos de todos los documentos. De la lista de textos se obtuvo la representación en: One Hot Encoding, frecuencia y TFIDF. Se realizó una función para que reciba el corpus y el índice de un documento y devuelva los documentos ordenados por la similitud coseno.</aside><br>

### [Desafío 2a](NLP/2a_bot_dnn_spacy_esp.ipynb) y [Desafío 2b](NLP/2b_bot_tfidf_nltk_world_cup.ipynb) 
<img src="https://github.com/strumiac/TrabajosPracticos/blob/main/4toBim/fig/2-bot.png" width="80" align="left">
<aside>En la notebook 2a se implementó un bot simple (SpotiBOT) que fue capaz de responder a diferentes tipos de preguntas con buena precisión. Se ensayó la técnica de filtrado de los stop words y se entrenó en modelo con BOW (ohe) y con TF-IDF. En la notebook 2b se analizó el bot desarrollado en clase con la librería NLTK y se utilizó como documento de entrada el artículo de Wikipedia de FIFA World Cup. Se utilizó la librería Sklearn para hacer TFIDF y la similitud coseno.</aside><br>

 ### [Desafío 3](NLP/3b_Custom_embedding_con_Gensim.ipynb)
<img src="https://github.com/strumiac/TrabajosPracticos/blob/main/4toBim/fig/3-embeddings.png" width="80" align="left">
<aside>Con el script estudiado en clase se crearon vectores con Gensim empleando el dataset de canciones de Nirvana. Al script se le modificó el tamaño de embeddings, modelo CBOW y frecuencia mínima. Se entrenó el modelo y se analizó la relación de ciertas palabras.</aside><br>

### [Desafío 4](NLP/4d_prediccion_palabra.ipynb)
<img src="https://github.com/strumiac/TrabajosPracticos/blob/main/4toBim/fig/4-next_word.png" width="80" align="left">
<aside>Se eligió el dataset de canciones de Nirvana para crear embeddings propios. Estos embeddings se utilizaron en diferentes arquitecturas (LSTM, LSTM bidireccional, capas hidden con más neuronas)para predecir la próxima posible palabra. Los resultados no fueron muy buenos debido a que se entrenaron los embeddings con un dataset pequeño.</aside><br>
 
### [Desafío 5a](NLP/5d_clothing_ecommerce_reviews.ipynb) y [Desafío 5b](NLP/5d_clothing_ecommerce_reviews_v2.ipynb) 
<img src="https://github.com/strumiac/TrabajosPracticos/blob/main/4toBim/fig/5-sentimental.png" width="80" align="left">
<aside>Se empleó el dataset clothing ecommerce reviews para entrenar un modelo que utilice las críticas de los compradores de ropa y determine la evaluación del comprador y su crítica (de 1 a 5 estrellas). Se realizó un EDA del dataset y preprocesamiento. Primero se entrenaron los embeddings propios y una arquitectura LSTM. Luego se aplicó transfer learning con embeddings de Fasttext. Por último, se entrenó el modelo haciendo un balance de clases (class weight).</aside><br>

### [Desafío 6](NLP/6_bot_qa.ipynb) 
<img src="https://github.com/strumiac/TrabajosPracticos/blob/main/4toBim/fig/6-bot_conversacional.png" width="80" align="left">
<aside>Se construyó un BOT que responda a la preguntas del usuario. Debido a que el dataset estaba en un formato json un poco complejo, los profesores facilitaron un script para levantar el dataset. Se siguieron algunas recomendaciones de los profesores para armar y entrenar el modelo. Cuando se ensayó el BOT, todas las respuestas arrojadas guardaron una coherencia aceptable y varias fueron correctas.</aside><br><br>

## Alumno
:pencil: Ing. Carlos Strumia (mail: strumiac@gmail.com)

Soy *Ingeniero Electromecánico con Orientación en Automatización Industrial* recibido de la Facultad de Ingeniería de la UNLPam/ Instituto Balseiro. Trabajo en el Departamento de Seguridad Nuclear de la Central Nuclear Atucha I y II.

Actualmente me encuentro cursando las últimas asignaturas de la Carrera de Especialización en Inteligencia Artificial (CEIA - FIUBA).

## Profesores
:octocat: Msc. Rodrigo Cardenas Szigety<br>
:octocat: Esp. Ing. Hernán Contigiani
