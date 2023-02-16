#!/bin/sh


echo "Enter two numbers: "
read num1
read num2

echo "The addition of $num1 and $num2 is `expr $num1 + $num2`."
echo "The subtraction of $num1 and $num2 is `expr $num1 - $num2`."