# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

RUN ["pip","install","flask"]

EXPOSE 9248

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=9248"]
