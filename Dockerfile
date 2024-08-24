FROM python:3.10-alpine3.15

WORKDIR /src

RUN apk add gcc
RUN apk add python3-dev

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /src