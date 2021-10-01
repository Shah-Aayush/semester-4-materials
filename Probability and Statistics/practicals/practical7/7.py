#!/usr/bin/env python3

#Scan an integer n from the user. Scan n sentences (no special character, punctuation, all lower case letters). Each sentence’s sentiment is either positive or negative. Scan 2 different words y and z from the user. y and z should be words from the set of distinct words constructed from n sentences. Write a program to estimate (i) the probability of y being present in the positive sentences (ii) the joint probability of y and z being present in positive sentences assuming that the presence of y and z in any sentence are independent events. What would be this probability if these events are not independent?

import string

def isValid(str):
	invalidChars = set(string.punctuation)
	if any(char in invalidChars for char in str) or any(char.isupper() for char in str):	#any function will return True if atleast one of the characters is in invalidChars.
		return False
	else:
		return True
	
sentences = []
words = []
positive_words = []
negative_words = []
sentiments = []

n = int(input("Enter number of sentences : "))

for index in range(n):
	sentences.append(str(input("\tEnter sentence {} : ".format(index+1))))
	while not isValid(sentences[index]):
		sentences[index] = str(input(f"\t\tEnter proper sentence {index+1} : "))
	words.extend(sentences[index].split())
	
	sentiments.append(int(input("\tEnter sentiment of the sentence [1 for positive; 2 for negative] : ")))
	while sentiments[index] not in [1,2]:
		sentiments[index] = int(input(f"\t\tEnter proper sentiment : "))
	
	if sentiments[index] == 1:
		positive_words.extend(sentences[index].split())
	else:
		negative_words.extend(sentences[index].split())
		
distinct_words = set(words)
#print(distinct_words)
	
y = str(input("Enter 1st word (y) : "))
while y not in distinct_words:
	y = str(input("\tEnter proper 1st word (y) : "))
	
z = str(input("Enter 2nd word (z) : "))
while z not in distinct_words:
	z = str(input("\tEnter proper 2nd word (z) : "))

p_of_y_present = positive_words.count(y)/len(positive_words)
p_of_yz_present_independent = (positive_words.count(y)/len(positive_words)) * (positive_words.count(z)/len(positive_words))

ans = 0
for index in range(n):
	if sentiments[index]==1 and (y in sentences[index]) and (z in sentences[index]):
		ans+=sentences[index].count(z)

p_of_yz_present_dependent = (ans*positive_words.count(y))/(len(positive_words))


print("The probability of y being present in the positive sentences is",p_of_y_present)
print("The probability of y and z being present [INDEPENDENT] in the positive sentences is",p_of_yz_present_independent)
print("The probability of y and z being present [  DEPENDENT] in the positive sentences is",p_of_yz_present_dependent)