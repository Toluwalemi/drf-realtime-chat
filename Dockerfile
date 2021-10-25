# pull official base image
FROM python:3.9.5-slim-buster

# set working directory
RUN mkdir /code
WORKDIR /code

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY entrypoint.sh /code/entrypoint.sh
COPY . /code/
RUN chmod +x entrypoint.sh

# add app


# run entrypoint.sh
#ENTRYPOINT ["/code/entrypoint.sh"]