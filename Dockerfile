FROM pondsregistry.azurecr.io/r-base:latest

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENV LD_LIBRARY_PATH=/usr/local/lib/R/lib/:${LD_LIBRARY_PATH}

ENV LISTEN_PORT 80
EXPOSE 80
