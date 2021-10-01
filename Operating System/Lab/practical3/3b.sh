#!/bin/bash

for number1 in 1 2 3;
do
	for number2 in 1 2 3;
	do
		for number3 in 1 2 3;
		do
			if [ $number1 != $number2 ] && [ $number1 != $number3 ] && [ $number2 != $number3 ];
			then
				echo "$number1 $number2 $number3";
			fi
		done
	done
done