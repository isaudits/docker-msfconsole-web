#!/bin/bash

docker build -t isaudits/msfconsole-web .
docker image prune -f