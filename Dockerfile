FROM python:3.8-alpine

RUN apk add --no-cache bash
ENV PYTHONUNBUFFERED 1

RUN mkdir /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

ADD . /usr/src/app
WORKDIR /usr/src/app
