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

if [ $operator = "1" ]
then
	echo "$n1 + $n2 "| bc -l
elif [ $operator = "2" ]
then  
	echo "$n1 - $n2 "| bc -l
elif [ $operator = "3" ]
then
	echo "$n1 * $n2 "| bc -l
elif [ $operator = "4" ]
then
	echo "$n1 / $n2 " | bc -l

fi