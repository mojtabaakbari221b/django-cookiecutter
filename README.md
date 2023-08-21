# django cookiecutter

## Prerequisites

#### install cookiecutter

```python
pip install cookiecutter
```

#### setup the project

```python
cookiecutter https://github.com/mojtabaakbari221b/django-cookiecutter
```

#### env file

create your env file and put your desired values instead of default:

```cp .envs/.env.sample .envs/.env```


#### install requirements

After creating the virtual environment, install the requirements :

‍‍‍‍```pip install -r requirements/development.txt   # for development```

```pip install -r requirements/production.txt   # for production```

## Pre-Run

run migration :

```./manage.py migrate```


## Run Project

#### run in development with manage command

```./manage.py runserver --settings configs.django.development```


#### run in production with manage command

```./manage.py runserver --settings configs.django.production```


#### run with gunicorn in production
```DJANGO_SETTINGS_MODULE=configs.django.production gunicorn configs.wsgi:application --bind 0.0.0.0:8000 --workers 3```

#### run with docker

```docker-compose -p local -f compose/local.yml up --build -d```
