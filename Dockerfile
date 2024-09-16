FROM python:3.10

WORKDIR /workdir

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY main.py .
COPY app app
COPY .env .env
COPY default.conf default.conf