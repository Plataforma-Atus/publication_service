

# pull oficial base image
FROM ubuntu:20.04
# set working directory
ARG DEBIAN_FRONTEND=noninteractive

# set environment variables

RUN apt-get update && apt-get install -y python3.9 python3.9-dev python3-pip unoconv poppler-utils git ghostscript

RUN pip install git+https://github.com/phgrigorio/python-docx
ADD . /code
WORKDIR /code

COPY poetry.lock /tmp/
COPY pyproject.toml /tmp/

RUN pip install poetry
RUN cd /tmp && poetry export --without-hashes -f requirements.txt --output /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


RUN rm -R /usr/share/fonts
RUN cp -R /code/fonts /usr/share/fonts
RUN fc-cache