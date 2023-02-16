#!/bin/sh


echo "Enter two numbers: "
read a 
read b 

if [ $a -gt $b ]; then
    echo "$a is greater than $b"
elif [ $a -eq $b ]; then
    echo "$a and $b are equal"
else
    echo "$b is greater than $a"
fi

