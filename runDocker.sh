#!/bin/bash

docker build -t todo_list_frontend .
docker run -dp 8000:8000 -v .:/app todo_list_frontend