import json
import os

from django.core.exceptions import ImproperlyConfigured

with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name,secret=secret):
    try:
        return secret[secret_name]
    except:
        msg = "La variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USUARIO'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# mysqlclient

MYSQL = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'mysqldb',
        'USER': 'juanel',
        'PASSWORD': '#Maremoto7674',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
