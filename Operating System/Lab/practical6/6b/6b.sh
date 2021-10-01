#!/bin/bash

#Write a shell script to concatenate all given file into a single file.
echo -n "Enter the number of files to be concatenate : "
read number
count=1
rm -f all.txt #delete the file if it exists.
while [ $count -le $number ]; do
	read file_name
	cat $file_name >> all.txt <(echo)		#here <(echo) will insert new line after cat appends each file.
	count=$((count+1))
done
echo "All files are concatenated in 'all.txt' file."