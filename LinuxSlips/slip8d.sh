#!/bin/sh


operand1=true
operand2=false

if [ "$operand1" = true -a "$operand2" = true ]; then
    echo "Both are true"
else
    echo "Both are not true"
fi


if true  &&  true 
then
    echo "Both are TRUE"
else
    echo "Both are not TRUE"
fi


echo "Enter two boolean values: "
read a
read b 

if $a && $b = true 
then
    echo "Both are true"
else
    echo "Both are not true"
fi