# `Real-time Chat` service

`Real-time Chat` service is a RESTful web service that uses Celery as its scheduler for realtime conversation.

## FEATURES
* Uses Celery for real-time chat
* No more than 90 messages are sent in an hour (Throttling)
* Prevents messages from being sent from 20:00 -09:00 taking into account different timezones
* Tests

## DOCUMENTATION
* http://localhost:8009/swagger-docs/
* http://localhost:8009/docs/

## RESTFUL ROUTES

```text
|Endpoints                  |HTTP Method   |CRUDMethod   |Result   |
|---------------------------|--------------|-------------|---------|
|/conversations/            |    GET       |     READ    | get all conversations
|/conversations/            |    POST      |     CREATE  | add a conversation
|/conversations/:id/        |    GET       |     READ    | get a conversation
|/conversations/:id/        |    PUT       |     UPDATE  | update an existing conversation
|/conversations/:id/        |    PATCH     |     UPDATE  | update one or more fields of an existing conversation
|/conversations/            |    DELETE    |     DELETE  | delete a conversation
|/chats/                    |    GET       |     READ    | get all chats
|/chat/                     |    POST      |     CREATE  | add a chat
|/chats/:id/                |    GET       |     READ    | get a single chat
|/chats/:id/                |    PUT       |     UPDATE  | update an existing chat
|/chats/:id/                |    PATCH     |     UPDATE  | update one or more fields of an existing chat
|/chats/:id/                |    DELETE    |     DELETE  | delete a chat
```

## General Usage

* Kindly run the project with Docker. 
* Clone the project.
* Create a **.env** in the project and copy the contents inside **.env-sample** into the newly
created **.env** file
* Run the docker-compose.yml file:
```bash
 docker-compose up --build
```
* Run Migrations:
```bash
 docker-compose exec web python manage.py makemigrations api
 docker-compose exec web python manage.py migrate
```
* App will be available at: http://0.0.0.0:8009
* Run the tests with this command:
```bash
 docker-compose exec web pytest
```
* You may create a superuser account to add data via the django-admin:
```bash
  docker-compose exec web python manage.py createsuperuser
```
* Or you can load the database with the data present in the fixtures folder:
```bash
  docker-compose exec web python manage.py loaddata fixture.json
```
* Go to http://0.0.0.0:8009/api to access the endpoints