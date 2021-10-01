#!/usr/bin/env python3

#	Assume that you are a professional fighter and in the past, you had fights with Undertaker. There were total of m (scan m from the user) fights between you and Undertaker. Assume that you set up a fresh fight tournament of n (scan n from the user) fights between you and Undertaker. Write a program which scans result of m earlier fights and computes the probability of (i) you wining x number of fights (ii) you winning more than y number of fights in the new tournament. Scan x and y from the user. Assume that fights are independent and each fight can either result in you or him winning. Assume that probability of you winning in each fight remains constant.

import random 

def factorial(number):
	answer = 1
	for num in range(number+1):
		answer *= (num+1)
	return answer

def combination(N,R):
	return (factorial(N)/(factorial(R)*factorial(N-R)))

def x_wins_out_of_n(x,n,probability_of_wins):
	return combination(n,x)*(probability_of_wins**x)*((1-probability_of_wins)**(n-x))

m = int(input("Enter m [total number of fights happened] : "))

result_of_fights = 0

#RANDOM PROCESS

result_list = [random.randint(0, 1) for i in range(m)]
print("Random generated data [1 for won, 0 for lose]: ",)
result_of_fights = result_list.count(1)


#MANUAL PROCESS

#print("Enter results for",m,"fights : [0 for loss;1 for win]")
#for index in range(m):
#	while True : 
#		str_input = "\tFor fight number " + str(index+1) + " : "
#		choice = int(input(str_input))
#		if(choice == 1 or choice == 0):
#			break
#		else:
#			print("Enter valid choice :(")
#	result_of_fights += choice
	
probability_of_wins = result_of_fights/m

n = int(input("Enter n [total number of fresh fights] : "))
x = int(input("Enter x [number of fights which you want to win] : "))

print("Probability of",x,"wins out of",n,"wins : ",x_wins_out_of_n(x, n, probability_of_wins))

y = int(input("Enter y [number of fights which atleast you want to win] : "))

probability_of_yPLUS_wins = 0
for fight_number in range(y+1,n):
	probability_of_yPLUS_wins += x_wins_out_of_n(fight_number, n, probability_of_wins)
	
print("Probability of more than",y,"wins : ", probability_of_yPLUS_wins)