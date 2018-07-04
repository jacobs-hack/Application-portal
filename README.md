# ApplicationPortal

A Django Application for the JacobsHack Portal. 
Adapated from https://github.com/JacobsAlumni/MemberManagement.

Deployable via docker, see [Dockerfile](Dockerfile) for settable variables. 

## Local Development
For hacking around, install python (>= 3.4) and run locally.
You are expected to be familiar with Django basics and virtualenv.
As a reminder:

```bash
# Setup a virtualenv
python -m virtualenv env

# Enter virtualenv
source env/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# run migrations
python manage.py migrate

# run a development server
python manage.py runserver
```

## Docker Deployment

This project has a Dockerfile and can be found on [DockerHub](https://hub.docker.com/r/jacobshack/portal/).

```bash

# Either build locally
docker build -t jacobshack/portal

# Or pull from from DockerHub (automated build)
# This will get you the latest version of the portal
docker pull jacobshack/portal

# you can alternatively use the prod tag:
docker pull jacobshack/portal:prod

# Run the docker container, all state is stored in an sqlite database
# see the Dockerfile for details
docker run -p 8080:80 -e DJANGO_SECRET_KEY=dummy -v data:/data/ jacobshack/portal
```

The database is stored inside the data volume. 
The CVs are stored in the subfolder cvs/ of the data volume. 