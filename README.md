# FOODGRAM
http://84.201.154.235/
login - bss.bzz@mail.ru
pass - 1234

This is a sample project that demonstrates how to use Docker Compose to run a web application with multiple services.

# Overview
The project consists of the following services:

db: A PostgreSQL database instance
backend: A Python Django backend application
frontend: A React frontend application
nginx: A reverse proxy server using NGINX
The docker-compose.yml file configures all of these services and sets up necessary dependencies between them. When you run docker-compose up, it will create and start all of the containers for these services.

# Getting Started

# Prerequisites
In order to run this project, you will need to have the following software installed:

Docker
Docker Compose

#Installing
Clone the repository:
git clone git@github.com:username/project.git

Navigate to the project directory:
cd project

Create a .env file for your environment variables:
cp .env.example .env

Update the environment variables in .env as needed.

# Running
To start the application, simply run:
docker-compose up

This will start all of the services in the background and output their logs to your console. You can access the application by visiting http://localhost in your web browser.

To stop the application, press Ctrl+C or run:
docker-compose down

# Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository
Create a feature branch (git checkout -b my-new-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin my-new-feature)
Create a new Pull Request

# How to use
Clone rep:
git clone https://github.com/andrewlegkii/foodgram-project-react.git

Login your server

Install DOCKER:
sudo apt install docker.io 

Install docker-compose:
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

Copy docker-compose.yaml amd nignix.conf to server: scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yaml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf

Create file .env by use file - env.e

Inatsall and activate virt env:
python -m venv venv 
source venv/Scripts/activate
python -m pip install --upgrade pip

Inatall all packages:
pip install -r requirements.txt

Start project in Docker:
sudo docker-compose up -d --build

Make some migrations:
sudo docker-compose exec backend python manage.py migrate

Create superusre:
sudo docker-compose exec backend python manage.py createsuperuser

Statistic:
sudo docker-compose exec backend python manage.py collectstatic --no-input

Text data:
sudo docker-compose exec backend python manage.py load_ingredients

To stop project:
docker-compose down -v

Add github action secrets:
DOCKER_USERNAME
DOCKER_PASSWORD
HOST
USER
SSH_KEY 
DB_ENGINE - django.db.backends.postgresql
DB_NAME
POSTGRES_USER
POSTGRES_PASSWORD
DB_HOST
DB_PORT
SECRET_KEY - django secret
ALLOWED_HOSTS - your server ip
TELEGRAM_TO - chat id
TELEGRAM_TOKEN - bot api

# Author
Andrew Legkii (https://github.com/andrewlegkii)