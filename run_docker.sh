#!/bin/bash
# get current dir
DIR=$(pwd -P)

# get relative path to source dir
FILE_DIR=`dirname ${BASH_SOURCE[0]}`

# save full path source dir
cd $FILE_DIR
FILE_DIR=$(pwd -P)

# go back to where we came from
cd $DIR

# run the container, mount the source dir into the container
docker run -it --rm -v $FILE_DIR:/home/repo drewpearce/trd-challenge:latest
