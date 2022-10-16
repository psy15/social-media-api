# social-media-sample-api

4 way chained dependent drop-down list in django (with ajax request) and mysql database

## Running the Project Locally

#### 1. Clone git repository

```bash
git clone "https://github.com/psy15/social-media-api.git"
```

#### 2. Install requirements

```bash
cd docial-media-api/
pip install -r requirements.txt
```

#### 3. Edit project settings

```bash
# open settings file in config

# Edit Database configurations with your Postgresql configurations.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database-name>',
        'USER': '<postgresql-user>',
        'PASSWORD': '<postgresql-password>',
        'HOST': '<postgresql-host>',
        'PORT': '<postgresql-port>',
    }
}


# save the file
```

#### 4. Runt tests

```bash
# Make migrations
python manage.py test
```

#### 5. Run the server

```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```
