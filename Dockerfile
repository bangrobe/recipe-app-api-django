FROM python:3.8-alpine

# MAINTAINER Bang Learn From Udemy

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# Cai dat postgres client
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

RUN pip install -r requirements.txt
# Delete temporary requirents
RUN apk del .tmp-build-deps

#Tao thu muc app trong docker image
RUN mkdir /app
# Thiet lap workdir la /app
WORKDIR /app
#Copy tu thu muc app tren local machine sang thu muc app cua docker
COPY ./app /app

# Them user vao Docker
RUN adduser -D user
USER user
