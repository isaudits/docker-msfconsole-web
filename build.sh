#!/bin/bash

#hooks/build
docker build -t isaudits/msfconsole-web .
docker image prune -f