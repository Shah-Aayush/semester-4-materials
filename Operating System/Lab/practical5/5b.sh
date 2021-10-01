#!/bin/bash

#Write a shell script which imitates tail command.

echo -n "Enter file name : "
read file_name

echo -n "Enter the number of lines : "
read number

#USE OF -n
printf "\nLast $number lines from file $file_name are : \n"
tail -n $number $file_name

#USE OF -c
printf "\n\nLast $number bytes from file $file_name are : \n"
tail -c $number $file_name

#USE OF -q
printf "\n\nLast 10 lines from file $file_name are [without showing file name] : \n"
tail -q $number $file_name

#USE OF -v
printf "\nLast 10 lines from file $file_name are [with showing file name]: \n"
tail -v $number $file_name
