#!/bin/sh


$path="/dev/stdout"

if [ -c /dev/stdout/ ]; then
    echo "$path is a character file"
else
    echo "$path is not a character file"
fi
