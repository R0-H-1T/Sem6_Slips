#!/bin/sh

$path="/dev/console"

if [ -b $path ]; then
    echo "$path is a block file"
else
    echo "$path is not a block file"
fi

