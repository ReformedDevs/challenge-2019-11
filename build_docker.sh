#!/bin/bash
# Assumes you have Docker and curl installed
TAG=latest
function pull {
    docker pull drewpearce/trd-challenge:$TAG
}

function build {
    mkdir -p /tmp/$TAG
    curl -o /tmp/$TAG/Dockerfile https://raw.githubusercontent.com/ReformedDevs/challenge-docker/$TAG/Dockerfile
    SRC=$(pwd)
    cd /tmp/$TAG
    docker build -t drewpearce/trd-challenge:$TAG .
    cd $SRC
}

pull || build
