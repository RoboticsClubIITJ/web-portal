### Installation:
Requirements:
- Python 3.6 runtime
- Django >= 2.1.6
- Other dependencies in `Pipfile`

Procedure:
- Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu).
- Navigate to the cloned repository.
    ```
    cd <project_directory_name>     # gymkhana_portal
    ```
- Install `pipenv` for dependency management
    ```
    pip install pipenv
    ```
- Copy `.env.example` to `.env`
    ```
    cp .env.example .env
    ```
- Use pipenv to install other dependencies from `Pipfile`
    ```
    pipenv install --dev
    ```
- Activate the new virtual environment
    ```
    pipenv shell
    ```
- Change to source code directory
    ```
    cd src
    ```
- Make database migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Create a superuser
    ```
    python manage.py createsuperuser
    ```
- Run development server on localhost
    ```
    python manage.py runserver :8000
    ```
#### Sarting Celery:
To perform asunc task we use celery [mail sending etc]
- In new terminal Run
    ```
    celery -A config worker -l INFO
    ```
#### DummyData for Testing [OPTIONAL]:
This will populate the database with random values for testing.
```
python manage.py createfixture 
```
