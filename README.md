- instalar Node.js (https://nodejs.org/en)
- en el directorio 'embebidos-proyect'
    - ```pip install -r requirements.txt```
- en webapp/api/migrations borrar las migraciones menos el _init_.py (tienen estilo 0001_initial.py etc)
- hacer ```cd webapp```
- ```pip install django```
- ```pip install djangorestframework```
- ```pip install django-crispy-forms```
- ```pip install crispy-bootstrap5```
- correr:
    1. ```python manage.py makemigrations``` (corre los modelos para creacion de base de datos, esto se tiene que correr cada vez que se haga un cambio en los modelos de datos)
    2. ```python manage.py migrate``` (ejecuta las migraciones)
    3. ```python manage.py createsuperuser``` (esto para crear un usuario administrador y poder usar la parte del admin, seguir instrucciones de consola)
    4. ```python manage.py runserver``` (corre la pagina en el ip que te pone)
- urls habilitadas estan en webapp/api/urls.py
- la app se divide en 2: 
    - webapp/webapp (aca estan los settings y cosas de las configuraciones más globales)
    - webapp/api (aca esta el contenido de la pagina)

