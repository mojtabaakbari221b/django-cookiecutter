FROM python:3.9
ENV HOME=/opt/projcet_name_celery/

# Set working directory
RUN mkdir -p $HOME
WORKDIR $HOME

# Installing requirements
COPY requirements $HOME/requirements
RUN pip install --upgrade pip
RUN pip install -r requirements/celery.txt

COPY configs $HOME/configs
# COPY projcet_name $HOME/projcet_name
