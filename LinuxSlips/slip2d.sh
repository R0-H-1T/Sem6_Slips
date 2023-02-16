#!/bin/sh

echo "Enter an operand:"
read num

echo "$num-- = `expr $num - 1`"
echo "$num++ = `expr $num + 1`"