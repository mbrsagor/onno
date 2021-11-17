# Onno
> Onno Backend API web Server.

### Setup
The following steps will walk you thru installation on a Mac. I think Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

#### Prerequisites
- Python3.8.5
- Django 3.1.6
- PostgreSQL 12.5

###### Create database 
> Open your terminal, shell, or ZSH
```base
psql postgres
create database "onno";
create user "onnoUser";
GRANT ALL PRIVILEGES ON DATABASE "onno" TO "onnoUser";
ALTER USER onnoUser CREATEDB;
CREATE EXTENSION postgis;
```

> Then go to config config/db_dev.config.py
###### Example:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'onno',
        'USER': 'onnoUser',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        # 'PORT': '',
    }
}
```

###### Backend server run locally.
> Please follow the instruction for run the backend server in your local dev server.
```base
git clone https://github.com/ProlificTechSolution-Onno/onno.git
cd onno
virtualenv venv --python=python3.8
source venv/bin/activate
./manage.py makemigrations accounts
./manage.py migrate accounts
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
