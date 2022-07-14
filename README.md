# notes-app

This is a simple CRUD notes application. 
Uses django on a backend and react for the frontend.

## Installation

```shell
python -m venv env
.\env\Scripts\activate
python -m pip install -r requirements.txt
python .\manage.py migrate 

cd interface
npm install
npm build
```

## Run
```shell
python manage.py runserver
```