#!/bin/sh

echo "Enter two numbers: "
read a 
read b

echo "$a + $b = `expr $a + $b`"
echo "$a++ = `expr $a + 1`"
echo "$b-- = `expr $b - 1`"
