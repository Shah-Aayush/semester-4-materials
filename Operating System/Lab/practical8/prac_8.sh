#!/bin/bash
while [ true ]
do
	printf "MENU : \n"
	printf "\t[1.] Insert a data\n"
	printf "\t[2.] Delete a data\n"
	printf "\t[3.] Modify a data\n"
	printf "\t[4.] Display data\n"
	printf "\t[5.] Exit\n"
	printf "Enter Choice : "
	read ch
	case $ch in
	1) printf "Enter roll number : "
			read roll_number
			printf "Enter name : "
			read name
			printf "Enter branch : "
			read branch
#			echo "" >> database.txt
			echo $roll_number"|"$name"|"$branch >> database.txt 
			echo "# Data inserted!"
			;;
	2) printf "Enter roll number to delete : "
			read roll_number
			grep -v $roll_number database.txt > temp_database.txt		#grep -v command returns all lines in file which do not match given the pattern (here, roll number)
			cat temp_database.txt > database.txt
			rm temp_database.txt
			echo "# Data deleted!"
			;;
	3) 	printf "\tSUB-MENU : \n"
		printf "\t\t[1.] Modify roll number only\n"
		printf "\t\t[2.] Modify name only\n"
		printf "\t\t[3.] Modify branch only\n"
		printf "\t\t[4.] Modify all\n"
		printf "\tEnter choice : "
		read choice
		case $choice in
		1)  printf "Enter roll number of student you want to update : "
			read old_roll_number
			echo "Enter new roll number : "
			read roll_number
			prev_name=`grep $old_roll_number database.txt | cut -d "|" -f2`			#extract only useful data. (here, in line, data is separated by ',' as specified by the option 'd' which means delimeter. and extracting the field number-2 as specified by -f2 [which is name of student])
			prev_branch=`grep $old_roll_number database.txt | cut -d "|" -f3`		#extract only useful data. (here, in line, data is separated by ',' as specified by the option 'd' which means delimeter. and extracting the field number-2 as specified by -f3 [which is branch of student])
			grep -v $old_roll_number database.txt > temp_database.txt
			cat temp_database.txt > database.txt
			rm temp_database.txt 
			echo "" >> database.txt
			echo $roll_number"|"$prev_name"|"$prev_branch >> database.txt 
			echo "# Data Modified!"
			;;
		2) 	printf "Enter roll number of student you want to update : "
			read old_roll_number
			echo "Enter new name : "
			read name
			prev_roll_number=`grep $old_roll_number database.txt | cut -d "|" -f1`			#extract only useful data. (here, in line, data is separated by ',' as specified by the option 'd' which means delimeter. and extracting the field number-2 as specified by -f1 [which is roll number of student])
			prev_branch=`grep $old_roll_number database.txt | cut -d "|" -f3`		#extract only useful data. (here, in line, data is separated by ',' as specified by the option 'd' which means delimeter. and extracting the field number-2 as specified by -f3 [which is branch of student])
			grep -v $old_roll_number database.txt > temp_database.txt
			cat temp_database.txt > database.txt
			rm temp_database.txt 
			echo "" >> database.txt
			echo $prev_roll_number"|"$name"|"$prev_branch >> database.txt 
			echo "# Data Modified!"
			;;
		3)  printf "Enter roll number of student you want to update : "
			read old_roll_number
			echo "Enter new branch : "
			read branch
			prev_roll_number=`grep $old_roll_number database.txt | cut -d "|" -f1`			#extract only useful data. (here, in line, data is separated by ',' as specified by the option 'd' which means delimeter. and extracting the field number-2 as specified by -f1 [which is roll number of student])
			prev_name=`grep $old_roll_number database.txt | cut -d "|" -f2`		#extract only useful data. (here, in line, data is separated by ',' as specified by the option 'd' which means delimeter. and extracting the field number-2 as specified by -f2 [which is name of student])
			grep -v $old_roll_number database.txt > temp_database.txt
			cat temp_database.txt > database.txt
			rm temp_database.txt 
			echo "" >> database.txt
			echo $prev_roll_number"|"$prev_name"|"$branch >> database.txt 
			echo "# Data Modified!"
			;;
		4)  printf "Enter roll number of student you want to update : "
			read roll_number
			grep -v $roll_number database.txt > temp_database.txt
			cat temp_database.txt > database.txt
			rm temp_database.txt 
			echo "Enter new roll number : "
			read roll_number
			echo "Enter new name : "
			read name
			echo "Enter new branch : "
			read branch
			echo "" >> database.txt
			echo $roll_number"|"$name"|"$branch >> database.txt 
			echo "# Data Modified!"
			;;
		*) echo "# Invalid choice!"
			;;
		esac ;;
	4) echo "DATA : "
			ARR1=('ROLL NUMBER|NAME|BRANCH')							#heading
			readarray -t ARR < <(cat database.txt | tr "\n" "\n")		# converting database.txt from single string to array to overcome 'too long line' error.
			ARR=("${ARR1[@]}" "${ARR[@]}")								# concatinating heading with database
			printf '%s\n' "${ARR[@]}" | column  -t -s '|'				# printing array as it's values separated from '|' and tabulizing it via column command.
		;; 
	5)  echo "THANK YOU!"
		break 
		;;
	*) echo "# Invalid choice!" ;;
	esac
done