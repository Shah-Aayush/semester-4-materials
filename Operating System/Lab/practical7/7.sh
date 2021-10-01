#Write a shell script for implementing directory management.

printf "*** DIRECTORY MANAGEMENT SYSTEM ***\n"
choice=0
while [ choice != 5 ] ; do
	printf "\n MAIN-MENU : \n"
	printf "\t[1] Create a new directory\n"
	printf "\t[2] Modify an existing directory\n"
	printf "\t[3] Navigate into directory\n"
	printf "\t[4] Listing directories\n"
	printf "\t[5] Exit\n"
	printf " Enter choice : "
	read choice

	case $choice in 
		1)
			printf "\tEnter directory name : "
			read file_name
			mkdir $file_name
			printf "\tFile named '$file_name' created in $PWD.\n"
		;;
		2)
			printf "\tEnter directory name : "
			read file_name
				printf "\tSUB-MENU : \n"
				printf "\t\t[1] Rename directory\n"
				printf "\t\t[2] Copy directory to another\n"
				printf "\t\t[3] Move directory\n"
				printf "\t\t[4] Delete directory\n"
				printf "\t\t[5] Exit from SUB-MENU\n"
				printf "\tEnter chioce : "
				read choice
				case $choice in 
					1)
						printf "\tEnter new name : "
						read new_name
						mv $file_name $new_name
						printf "\tFile '$file_name' renamed to '$new_name'.\n"
					;;
					2)
						printf "\tEnter target directory path : "
						read target
						cp -R $file_name $target
						printf "\tFile '$file_name' copied into '$target'.\n"
					;;
					3)
						printf "\tEnter target directory path : "
						read target
						mkdir $target
						mv $file_name $new_name
						printf "\tFile '$file_name' moved to '$target'.\n"
					;;
					4)
						printf "\tFile '$file_name' will be deleted permanently. Are you sure ? \n"
						printf "\t\t[1] YES\n"
						printf "\t\t[2] NO\n"
						printf "\t Enter choice : "
						read choice
						if [ $choice==1 ]; 
						then
							rmdir $file_name
							printf "\tFile '$file_name' deleted successfully.\n"
						else
							printf "\tDeletion operation cancelled.\n"
						fi
					;;
					5)
						printf "\tEXITED from SUB-MENU.\n"
					;;
					*)
						printf "\tInvalid choice :(\n"
				esac
			choice=0 #reset choice variable
		;;
		3)
			printf "\tSUB-MENU : \n"
			printf "\t\t[1] Go to parent directory\n"
			printf "\t\t[2] Go to specific directory\n"
			printf "\t\t[3] Exit from SUB-MENU\n"
			printf "\tEnter chioce : "
			read choice
			case $choice in 
				1)
					cd ..
					printf "\tWorking directory changed to '$PWD'.\n"
				;;
				2)
					printf "\tEnter directory path : "
					read target
					cd $target
					printf "\tWorking directory changed to '$PWD'.\n"
				;;
				3)
					printf "\tEXITED from SUB-MENU.\n"
				;;
				*)
					printf "\tInvalid choice :(\n"
					esac
					choice=0 #reset choice variable
		;;
		4)
			printf "\tSUB-MENU : \n"
			printf "\t\t[1] List directories\n"
			printf "\t\t[2] List directories with details.\n"
			printf "\t\t[3] Exit from SUB-MENU\n"
			printf "\tEnter chioce : "
			read choice
			case $choice in 
				1)
					printf "\tList of directories : \n"
					ls
				;;
				2)
					printf "\tDetailed list of directories : \n"
					ls -l
				;;
				3)
					printf "\tEXITED from SUB-MENU.\n"
				;;
				*)
					printf "\tInvalid choice :(\n"
					esac
					choice=0 #reset choice variable
		;;
		5)
			printf " EXITED."
			break 
		;;
		*)
			printf " Invalid choice :(\n"
		;;
	esac
		
done