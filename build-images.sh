#!/bin/sh

docker image build -t mhadam/transmission -f ./docker/transmission.df .
docker image build -t mhadam/clutch -f ./docker/clutch.df .
