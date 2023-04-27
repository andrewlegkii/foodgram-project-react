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
cp .env.e .env

Update the environment variables in .env as needed.

# Running
To start the application, simply run:
docker-compose up

This will start all of the services in the background and output their logs to your console. You can access the application by visiting http://localhost:8000 in your web browser.

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
1. Clone rep:
git clone https://github.com/andrewlegkii/foodgram-project-react.git

2. Login your server

3. Install DOCKER:
sudo apt install docker.io 

4. Install docker-compose:
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

5. Copy docker-compose.yaml and nignix.conf to server: scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yaml
scp nginx.conf <username>@<host>:/home/<username>/nginx.conf

6. Create file .env by use file - env.e

7. Inatsall and activate virt env:
python -m venv venv 
source venv/Scripts/activate
python -m pip install --upgrade pip

8. Inatall all packages:
pip install -r requirements.txt

9. Start project in Docker:
sudo docker-compose up -d --build

10. Make some migrations:
sudo docker-compose exec backend python manage.py migrate

11. Create superusre:
sudo docker-compose exec backend python manage.py createsuperuser

12. Statistic:
sudo docker-compose exec backend python manage.py collectstatic --no-input

13. Text data:
sudo docker-compose exec backend python manage.py load_ingredients

14. To stop project:
docker-compose down -v

15. Add github action secrets:
1) DOCKER_USERNAME
2) DOCKER_PASSWORD
3) HOST
4) USER
5) SSH_KEY 
6) DB_ENGINE - django.db.backends.postgresql
7) DB_NAME
8) POSTGRES_USER
9) POSTGRES_PASSWORD
10) DB_HOST
11) DB_PORT
12) SECRET_KEY - django secret
13) ALLOWED_HOSTS - your server ip
14) TELEGRAM_TO - chat id
15) TELEGRAM_TOKEN - bot api

# Author
Andrew Legkii (https://github.com/andrewlegkii) - backend
Yandex - frontend