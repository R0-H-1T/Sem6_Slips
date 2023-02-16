#!/bin/sh



for dir in /home/rohit/shellscripting/slips/*; 
do
    echo "$(basename "$dir")"
done


for a in $(ls */ -d)
do
    echo $a
done

ls -R