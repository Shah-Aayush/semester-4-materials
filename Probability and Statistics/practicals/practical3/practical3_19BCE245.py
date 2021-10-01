import array as arr

k = int(input("\nEnter the number of mutually exclusive and exhaustive events (k) : "))

events = arr.array('d')		# stores P(E1),P(E2),P(E3),...P(Ek)
print("\nEnter probability of each of the", k , "events : ")
for event in range(0,k):
	print("\tFor event",event+1,": ",end="")
	events.append(float(input()))
	
conditional_events = arr.array('d')		# stores P(B|E1),P(B|E2),P(B|E3),...P(B|Ek)
print("\nEnter probability of occurrence of event B assuming that each  of the", k , "events has occurred : ")
for conditional_event in range(0,k):
	print("\tFor event",conditional_event+1,": ",end="")
	conditional_events.append(float(input()))
	
p_of_B = 0
for index in range(0,k):
	p_of_B += conditional_events[index]*events[index]
	
print("Probability calculated through Bayes's theorem : ")
for index in range(0,k):
	print("\tP(E{}|B) = {}".format(index+1,round((conditional_events[index]*events[index])/p_of_B,2)))