import array as arr

k = int(input("\nEnter the number of mutually exclusive and exhaustive events (k) : "))

sum_of_events = 0

events = arr.array('d')		# stores P(E1),P(E2),P(E3),...P(Ek)
print("\nEnter probability of each of the", k , "events : ")
for event in range(0,k):
	print("\tFor event",event+1,": ",end="")
	x = float(input())
	if(x>=0 and x<=1):
		events.append(x)
		sum_of_events += x
	else:
		while(x<0 or x>1):
			x = float(input("Enter value between 0 and 1 : "))
		events.append(x)
		sum_of_events += x

if(sum_of_events == 1):
	conditional_events = arr.array('d')		# stores P(B|E1),P(B|E2),P(B|E3),...P(B|Ek)
	print("\nEnter probability of occurrence of event B assuming that each  of the", k , "events has occurred : ")
	for conditional_event in range(0,k):
		print("\tFor event",conditional_event+1,": ",end="")
		y = float(input())
		if(y>=0 and y<=1):
			conditional_events.append(y)
		else:
			while(y<0 or y>1):
				y = float(input("Enter values between 0 and 1 : "))
			conditional_events.append(y)
				
	p_of_B = 0
	for index in range(0,k):
		p_of_B += conditional_events[index]*events[index]
		
	print("\nProbability calculated through Bayes's theorem : ")
	for index in range(0,k):
		print("\tP(E{}|B) = {}".format(index+1,round((conditional_events[index]*events[index])/p_of_B,2)))
else:
	print("Invalid values as sum of all events is not equal to 1.")