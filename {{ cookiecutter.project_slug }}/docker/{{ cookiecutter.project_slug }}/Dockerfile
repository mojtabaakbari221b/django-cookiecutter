FROM python:3.9
LABEL MAINTAINER="{{ cookiecutter.project_slug }} | https://{{ cookiecutter.project_slug }}.com"
LABEL VERSION="0.0.0.1"

ENV PYTHONUNBUFFERED 1

ENV HOME=/opt/{{ cookiecutter.project_slug }}/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
ADD requirements/base.txt $HOME
RUN pip install --upgrade pip
RUN pip install -r base.txt

COPY .envs $HOME/.envs
COPY configs $HOME/configs
COPY manage.py $HOME
COPY {{ cookiecutter.project_slug }} $HOME/{{ cookiecutter.project_slug }}
COPY docker/{{ cookiecutter.project_slug }}/entrypoints/* $HOME
