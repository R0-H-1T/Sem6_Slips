#!/bin/sh

# chmod +x filename.sh

echo "Enter two values:"
read a
read b
#read -r num1 num2



echo "The modulus of $a and $b is `expr $a \% $b`"
#echo "The modulus of $a and $b is $((a % b))" // OR

echo "The multiplication of $a and $b is `expr $a \* $b`"
