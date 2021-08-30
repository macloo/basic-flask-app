FROM ubuntu:20.04
USER root
COPY ./static/css/main.css ./flask-py-basic-app/static/css/main.css
COPY ./static/images/* ./flask-py-basic-app/static/images/
COPY ./template/ ./flask-py-basic-app/templates/
COPY * ./flask-py-basic-app/
WORKDIR /flask-py-basic-app
RUN apt-get update && apt-get install -y
RUN apt install python3-pip -y
RUN pip install Flask
ENTRYPOINT ["python3"]
CMD ["routes.py"]
