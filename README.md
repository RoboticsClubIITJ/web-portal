# Robotics Club Web Portal [![Build Status](https://travis-ci.org/RoboticsClubIITJ/web-portal.svg?branch=master)](https://travis-ci.org/RoboticsClubIITJ/web-portal) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg) ![Django 2.2.9](https://img.shields.io/badge/Django-2.2.9-green.svg) ![Vue 2.6.11](https://img.shields.io/badge/Vue-2.6.11-green.svg)
<a href="http://roboticsiitj.in/">
        <img src="https://img.shields.io/badge/Deployed%20on%20DigitalOcean-blueviolet?style=plastic&logo=DigitalOcean"
</a>

## Getting Started

### Without Docker

To start your frontend and backend server individually:<br>
Follow the [Backend Readme](https://github.com/RoboticsClubIITJ/web-portal/tree/master/backend) to setup your backend server<br>
Follow the [Frontend Readme](https://github.com/RoboticsClubIITJ/web-portal/tree/master/frontend) to setup the frontend server<br>

### With Docker

Ensure that you have installed [Docker](https://docs.docker.com/install/) (with [Docker Compose](https://docs.docker.com/compose/install/)).

Run the development server:
```
cd <project_directory_name>
make dev-start
```

After executing `make dev-start`, you will be running:
* The application on http://localhost:8080 
* The API Server on http://localhost:8000

Make database migrations: 
```
make exec
python manage.py makemigrations
python manage.py migrate
```

Create a superuser: 
```
make exec
python manage.py createsuperuser
```

View logs of docker containers: 
```
make dev-logs
```

To stop the development server: 
```
make dev-stop
