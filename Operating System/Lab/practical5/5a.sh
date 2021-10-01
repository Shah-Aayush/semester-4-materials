#!/bin/bash

#Write a shell script which imitates head command.

echo -n "Enter file name : "
read file_name

echo -n "Enter the number of lines : "
read number

#USE OF -n
printf "\nFirst $number lines from file $file_name are : \n"
head -n $number $file_name

#USE OF -c
printf "\nFirst $number bytes from file $file_name are : \n"
head -c $number $file_name

#USE OF -q
printf "\n\nFirst 10 lines from file $file_name are [without showing file name] : \n"
head -q $number $file_name

#USE OF -v
printf "\nFirst 10 lines from file $file_name are [with showing file name]: \n"
head -v $number $file_name