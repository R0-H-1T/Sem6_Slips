#!/bin/sh


if [ -c /dev/tty ]; then
    echo "Is a character file"
else
    echo "Is not a character file"
fi