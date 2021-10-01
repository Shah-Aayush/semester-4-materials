#Simple calculator using conditional loop
while 1:
	print("\nSelect Operation : \n0. Exit\n1. Add\n2. Subtraction \n3. Multiply\n4. Divide")
	choice = int(input("Select operations from 0,1,2,3,4 : "))
	if(choice == 0):
		print("Thank you")
		break
	
	elif(choice == 1):
		n1 = int(input("Enter first number : "))
		n2 = int(input("Enter second number : "))
		ans = n1+n2
		print(n1 , " + " , n2 , " = " , ans)
		
	elif(choice == 2):
		n1 = int(input("Enter first number : "))
		n2 = int(input("Enter second number : "))
		ans = n1-n2
		print(n1 , " - " , n2 , " = " , ans)
		
	elif(choice == 3):
		n1 = int(input("Enter first number : "))
		n2 = int(input("Enter second number : "))
		ans = n1*n2
		print(n1 , " * " , n2 , " = " , ans)
		
	elif(choice==4):
		n1 = int(input("Enter first number : "))
		n2 = int(input("Enter second number : "))
		ans = n1/n2
		print(n1 , " / " , n2 , " = " , ans)
		
	else:
		print("Invalid choice")