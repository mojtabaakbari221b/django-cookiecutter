FROM python:3.9
ENV HOME=/opt/{{ cookiecutter.project_slug }}_celery/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
COPY requirements $HOME/requirements
RUN pip install --upgrade pip
RUN pip install -r requirements/celery.txt

COPY configs $HOME/configs
# COPY {{ cookiecutter.project_slug }} $HOME/{{ cookiecutter.project_slug }}
