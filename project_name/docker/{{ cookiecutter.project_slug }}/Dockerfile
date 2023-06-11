FROM python:3.9
LABEL MAINTAINER="projcet_name | https://projcet_name.com"
LABEL VERSION="0.0.0.1"

ENV PYTHONUNBUFFERED 1

ENV HOME=/opt/projcet_name/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
ADD requirements/base.txt $HOME
RUN pip install --upgrade pip
RUN pip install -r base.txt

COPY configs $HOME/configs
COPY manage.py $HOME
COPY projcet_name $HOME/projcet_name
COPY docker/projcet_name/entrypoints/* $HOME
