# pull oficial base image
#FROM python:3.9.1-slim-buster
FROM ubuntu:20.04
# set workinng directory

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3.9 python3.9-dev python3-pip
# set environment variables
RUN apt-get -y install python3-pip
ADD . /code
WORKDIR /code

COPY poetry.lock pyproject.toml /tmp/


RUN pip install poetry
RUN cd /tmp && poetry export -f requirements.txt --output /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


