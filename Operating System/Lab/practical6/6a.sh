#!/usr/bin/env python3

#Write a shell script to generate the series of number multiply by 2.
echo -n "Enter the number : "
read number
echo -n "Enter the count : "
read count

echo "Series of number multiply by 2 is :"
counter=1
while [ "$counter" -le "$count" ]; do
	counter=$((counter+1))
	number=$((number * 2))
	echo $number
done
