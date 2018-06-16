# ApplicationPortal

A Django Application for the JacobsHack Portal. 
Adapated from https://github.com/JacobsAlumni/MemberManagement.

Deployable via docker, see [Dockerfile](Dockerfile) for settable variables. 

## Local Development
For hacking around, install python (>= 3.4). 

You are expected to be familiar with Django basics and virtualenv. 

As a reminder:

```bash
# Setup a virtualenv
python3 -m virtualenv env

# Enter virtualenv
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# run a development server
python3 manage.py runserver
```