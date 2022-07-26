FROM tiangolo/uwsgi-nginx-flask:python3.8
ENV STATIC_INDEX 1
COPY ./app /app