#!/bin/sh

echo "Enter two boolean values: "

read a 
read b

if $a || $b = true
then
    echo "Either of the two is true"
else
    echo "None are true"
fi