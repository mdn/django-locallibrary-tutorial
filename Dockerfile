FROM python:3.8

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY . /opt/catalog
WORKDIR /opt/catalog

EXPOSE 50051
CMD [ "python", "manage.py", "runserver", "0.0.0.0:50051"]
