# Flask Boilerplate for Profesional Development

## Instalación (Windows)
- [Python 3.10.2](https://www.python.org/downloads/release/python-3102/)
- Copiar el .env.example con: `cp .env.example .env`
- Instalar pipenv: `pip install --user pipenv`
- De momento no usaremos bases de datos relacionales por lo que no hace falta instalar MySQL o Postgres
- Habilitar en las variables de entorno de Windows, el comando de pipenv. Para esto, abrir el ejecutador de windows (Run) y colocar: `%AppData%`
- - Una vez abierta la carpeta AppData, navegar hasta: `\Roaming\Python\Python310\Scripts`, donde veremos el archivo `pipenv.py`
- - Abrir la ventana de Variables de Entorno, en variables de entorno del usuario debemos buscar la propiedad `Path`, y a continuación agregar la dirección de la carpeta donde se encuentran los scripts de Python.
- - Al abrir nuevamente el comando de sistema (o reiniciar Visual Studio Code), debería reconocer el comando `pipenv`
- - En la carpeta del proyecto, abrir el comando de sistema es instalar las dependencias en un entorno virtual con: `pipenv install`

## Ejecutar el Boilerplate:

- Lo primero será activar el entorno virtual creado para este proyecto, el cuál tendrá sus propias librerías independientemente a las instaladas en el sistema. Usar el comando: `pipenv shell`
-Una vez ejecutado el entorno virtual, activaremos Flask con el comando preconfigurado: `pipenv run start`

## Features

- Extensive documentation [here](https://github.com/4GeeksAcademy/flask-rest-hello/tree/master/docs).
- Integrated with Pipenv for package managing.
- Fast deloyment to heroku with `$ pipenv run deploy`.
- Use of `.env` file.
- SQLAlchemy integration for database abstraction.

## Installation (automatic if you are using gitpod)

> Important: The boiplerplate is made for python 3.10.2 but you can easily change the `python_version` on the Pipfile.

The following steps are automatically runned withing gitpod, if you are doing a local installation you have to do them manually:

```sh
pipenv install;
mysql -u root -e "CREATE DATABASE example";
pipenv run init;
pipenv run migrate;
pipenv run upgrade;
```

## How to Start coding?

There is an example API working with an example database. All your application code should be written inside the `./src/` folder.

- src/main.py (it's where your endpoints should be coded)
- src/models.py (your database tables and serialization logic)
- src/utils.py (some reusable classes and functions)
- src/admin.py (add your models to the admin and manage your data easily)

For a more detailed explanation, look for the tutorial inside the `docs` folder.

## Remember to migrate every time you change your models

You have to migrate and upgrade the migrations for every update you make to your models:
```
$ pipenv run migrate (to make the migrations)
$ pipenv run upgrade  (to update your databse with the migrations)
```


# Manual Installation for Ubuntu & Mac

⚠️ Make sure you have `python 3.6+` and `MySQL` installed on your computer and MySQL is running, then run the following commands:
```sh
$ pipenv install (to install pip packages)
$ pipenv run migrate (to create the database)
$ pipenv run start (to start the flask webserver)
```


## Deploy to Heroku

This template is 100% compatible with Heroku[https://www.heroku.com/], just make sure to understand and execute the following steps:

```sh
// Install heroku
$ npm i heroku -g
// Login to heroku on the command line
$ heroku login -i
// Create an application (if you don't have it already)
$ heroku create <your_application_name>
// Commit and push to heroku (commited your changes)
$ git push heroku main
```
:warning: For a more detailed explanation on working with .env variables or the MySQL database [read the full guide](https://github.com/4GeeksAcademy/flask-rest-hello/blob/master/docs/DEPLOY_YOUR_APP.md).
