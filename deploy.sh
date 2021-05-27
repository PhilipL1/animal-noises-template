#!/bin/bash

project_name= animal_noises

sudo docker build -t $(project_name)_server server

sudo docker build -t $(project_name)_api animal_api

sudo docker network create $(project_name)_network 

sudo docker run -d \ 
    -p 5000:5000 \
    --name $(project_name)_server \
    --network $(project_name)_network \
    $(project_name)_server

sudo docker run -d \ 
    --name $(project_name)_api \
    --network $(project_name)_network \
    $(project_name)_api
