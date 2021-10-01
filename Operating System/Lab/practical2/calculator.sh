echo "Enter operation : "

echo "1. + (press 1) 
2. - (press 2) 
3. * (press 3) 
4. / (press 4)"

read operator

echo -n "Enter first number : "
read n1

echo -n "Enter second number : "
read n2

echo -n "Answer : "

case $operator in

    1) echo "$n1 + $n2" | bc -l;;

    2) echo "$n1 - $n2 "| bc -l;;

    3) echo "$n1 * $n2 "| bc -l;;

    4) echo "$n1 / $n2 "| bc -l;;

   *) echo "Invalid operator";;

esac