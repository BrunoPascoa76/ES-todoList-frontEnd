#!/bin/bash

docker build -t customerapi .
docker run -dp 8000:8000 --env-file=.env -v ./app:/app frontend