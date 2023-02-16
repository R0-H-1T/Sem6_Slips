#!/bin/sh

echo "Enter two numbers: "
read a 
read b 
echo "The multiplication of $a and $b is `expr $a \* $b`" 
echo "The subtraction of $a and $b is `expr $a - $b`" 