#!/bin/bash

docker stop vss-backend
docker container rm vss-backend
docker image rm vss-flask
docker build --tag vss-flask .
#docker run --network=host --name vss-backend -e DB_URL='postgresql://postgres:password@localhost/blk' vss-flask
docker save --output="vss-docker.tar" vss-flask
scp ./vss-docker.tar ubuntu@192.168.0.12:/home/ubuntu
