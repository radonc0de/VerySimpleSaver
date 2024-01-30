# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "api.py" ]

#docker run --network=host --name vss-backend -e DB_URL='postgresql://username:password@localhost/db-name' vss-flask
