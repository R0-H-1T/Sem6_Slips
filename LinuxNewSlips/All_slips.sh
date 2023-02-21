


even_or_odd(){
    echo "Enter a number: "
    read num
    if [ $[ $num % 2] -eq 0 ]; then
        echo "$num is even"
    else
        echo "$num is odd"
    fi
}


#even_or_odd




greater_than(){
    echo "Enter 3 numbers: "
    read a b c 

    if [ $a -gt $b ] && [ $a -gt $c ];
    then 
        echo "$a is greater than $b and $c"
    elif [ $b -gt $a ] && [ $b -gt $c ];
    then
        echo "$b is greater than $a and $c"
    else
        echo "$c is greater than $a and $b"
    fi

}   

#greater_than


table_of_num(){
    echo "Enter a number: "
    read num

    for i in {1..10}
    do
        echo "$num X $i  =  `expr $i \* $num`"
    done
}

#table_of_num



equal_string(){
    echo "Enter first string: "
    read str1
    echo "Enter second string: "
    read str2
    
    if [ $str1 == $str2 ]
    then
        echo "$str1 and $str2 are equal"
    else
        echo "$str1 and $str2 are not equal"
    fi
}

#equal_string


sum_of_digits(){
    echo "Enter a number: "
    read num 
    temp=$num
    
    sum=0
    while [ $temp -ne 0 ]
    do
        r=$(( $temp % 10 ))
        sum=$(( $sum + $r ))
        temp=$(( $temp / 10 ))
        # r=`expr $temp \% 10`
        # sum=`expr $sum + $r`
        # temp=`expr $temp / 10`
    done
    echo "Sum of digits of $num is $sum"
    return $sum
}

#sum_of_digits



reverse_number(){
    echo "Enter a number: "
    read num
    temp=$num

    reverse=0
    while [ $temp -ne 0 ]
    do
        r=$(( $temp % 10 ))
        reverse=$(( $reverse + $r ))
        reverse=$(( $reverse * 10 ))
        temp=$(( $temp / 10 ))
    done
    echo "Reverse of $num is $(( $reverse / 10 ))"
}
reverse_number