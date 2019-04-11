SecretSanta installation from scratch
==================


Install dependencies:
```
sudo apt-get install python3-pip rabbitmq-server postfix
sudo pip3 install virtualenv
```

Setup env:
```
mkdir secret_santa
cd secret_santa
virtualenv env
source env/bin/activate
```
Setup project:
copy santa_project src folder to santa_project project
```
cd santa_project
pip install -r requirements.txt 
./manage.py migrate
./manage.py createsuperuser
cd santa_app
celery worker -A tasks
```

Usage: 

Run tests:
```
./manage.py test santa_app
```
Run app:
```
./manage.py runserver
```

Register users here:
```
http://localhost:8000/santa/
```

Create pairs and send emails:
```
http://localhost:8000/admin/santa_app/pair/
```
