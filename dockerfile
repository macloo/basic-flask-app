FROM ubuntu:20.04
USER root
COPY * ./flask-py-basic-app/
WORKDIR /flask-py-basic-app
RUN apt-get update && apt-get install -y
RUN apt install python3-pip -y
RUN pip install Flask
ENTRYPOINT ["python3"]
CMD ["routes.py"]
