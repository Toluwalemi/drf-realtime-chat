# `Robots Competition` service

`Real-time Chat` service is a RESTful web service that uses Celery as its scheduler for realtime conversation.

## FEATURES
* No more than 90 messages are sent in an hour
* Prevents messages from being sent from 20:00 -09:00 taking into account different timezones
* Ordering and Pagination
* Authentication and Permissions
* Throttling
* Tests

## DOCUMENTATION


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
|/chats/                    |    POST      |     CREATE  | add a chat
|/chats/:id/                |    GET       |     READ    | get a single chat
|/chats/:id/                |    PUT       |     UPDATE  | update an existing chat
|/chats/:id/                |    PATCH     |     UPDATE  | update one or more fields of an existing chat
|/chats/:id/                |    DELETE    |     DELETE  | delete a chat
```

## General Usage

* Clone the repository
* Create a virtual environment in the folder. (If you are on linux, use the command below):
```bash
 python3.9 -m venv venv
```
* Activate the virtual environment (If you are on linux, use the command below):
```bash
 source venv/bin/activate
```
* Install the requirements:
```bash
 pip install -r requirements.txt
```
* Make migrations:
```bash
 python manage.py makemigrations api
 python manage.py migrate
```
* Run the command below to run the tests
```
 pytest
```
* Run the DJANGO's server and access the endpoints
```
 python manage.py runserver
```

