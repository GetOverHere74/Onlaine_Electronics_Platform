FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY /requirements.txt /

RUN pip install -r /requirements.txt --no-cache-dir

COPY . .
