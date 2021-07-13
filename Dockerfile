FROM python:3.8-alpine

# MAINTAINER Bang Learn From Udemy

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

#Tao thu muc app trong docker image
RUN mkdir /app
# Thiet lap workdir la /app
WORKDIR /app
#Copy tu thu muc app tren local machine sang thu muc app cua docker
COPY ./app /app

# Them user vao Docker
RUN adduser -D user
USER user
