FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app

COPY . .

ENV LISTEN_PORT 8080

EXPOSE 8080
