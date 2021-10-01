#!/bin/bash

#Write a shell script to keep on accepting lines of text and write the text into a data file until the user inputs "end". The script should count the number of lines input and display them.

echo "Enter lines to add them into data.txt [write 'end' for exit] : "
read_line=""
count_lines=0

rm -f write.txt #delete the file if it exists.

while [ "$read_line" != "end" ]; do
	read read_line
	if [ "$read_line" != "end" ]; then
		echo $read_line >> write.txt
		count=$((count+1))
	fi
done

printf "Total number of lines written : $count\nContent of the file : \n"
cat write.txt