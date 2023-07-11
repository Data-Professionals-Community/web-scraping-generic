FROM --platform=linux/amd64 python:3.10.10-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt