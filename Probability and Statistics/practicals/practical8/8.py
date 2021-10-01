#!/usr/bin/env python3

# Scan an integer n from the user. Scan n sentences (no special character, punctuation, all lower case letters). Each sentence’s sentiment is either positive or negative. Scan 5 words- a, b, c, d and e from the user. a, b, c, d, and e should be words from the set of distinct words constructed from n sentences. a, b, c, d, and e need not to be distinct words. Write a program to estimate (i) the joint probability of sampling a, b, c, d, and e from positive sentences. Assume that events of sampling a word are independent and the probability of sampling any word remains constant over different trials of sampling events.

import string
import math

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

a = str(input("Enter 1st word (a) : "))
while a not in distinct_words:
    a = str(input("\tEnter proper 1st word (a) : "))
    
b = str(input("Enter 2nd word (b) : "))
while b not in distinct_words:
    b = str(input("\tEnter proper 2nd word (b) : "))
    
c = str(input("Enter 3rd word (c) : "))
while c not in distinct_words:
    c = str(input("\tEnter proper 3rd word (c) : "))
    
d = str(input("Enter 4th word (d) : "))
while d not in distinct_words:
    d = str(input("\tEnter proper 4th word (d) : "))
    
e = str(input("Enter 5th word (e) : "))
while e not in distinct_words:
    e = str(input("\tEnter proper 5th word (e) : "))
    
p_of_a = positive_words.count(a)/len(positive_words)
p_of_b = positive_words.count(b)/len(positive_words)
p_of_c = positive_words.count(c)/len(positive_words)
p_of_d = positive_words.count(d)/len(positive_words)
p_of_e = positive_words.count(e)/len(positive_words)
    
print(p_of_a,p_of_b,p_of_c,p_of_d,p_of_e)

probability = math.factorial(len(positive_words)) / (math.factorial(positive_words.count(a)) * math.factorial(positive_words.count(b)) * math.factorial(positive_words.count(c)) * math.factorial(positive_words.count(d)) * math.factorial(positive_words.count(e)))

print(probability)

probability *= pow(p_of_a, positive_words.count(a)) * pow(p_of_b, positive_words.count(b)) * pow(p_of_c, positive_words.count(c)) * pow(p_of_d, positive_words.count(d)) * pow(p_of_e, positive_words.count(e))

print(positive_words)

print("Joint Probability : ",probability)