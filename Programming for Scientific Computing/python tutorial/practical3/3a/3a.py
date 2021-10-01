#number of alphabets,blank spaces, lowercase letter, uppercase letters, number of words starting from vowel, frequency of each word.
poem_file = open("poem.txt") #by default opens in read mode.
content = poem_file.read()

alphabets = 0
blank_spaces = 0
lowercase = 0
uppercase = 0
words_starting_from_vowels = 0

for i in range(len(content)):
	if(content[i].isalpha()):
		alphabets += 1
		if(content[i].islower()):
			lowercase += 1
		if(content[i].isupper()):
			uppercase += 1
	elif(content[i] == ' '):
		blank_spaces += 1
	if(i==0 or content[i] == ' ' or content[i] == '\n'):
		if(i+1<len(content)):
			if(content[i+1]) in ['a','e','i','o','u','A','E','I','O','U']:
				words_starting_from_vowels += 1
		else:
			continue
		
		
print("Content in the file : ")
print(content,"\n")

print("Number of alphabets : ",alphabets)
print("Number of lowercase letters : ",lowercase)
print("Number of uppercase letters : ",uppercase)
print("Number of blanck spaces : ",blank_spaces)
print("Number of words begin with vowel : ",words_starting_from_vowels)

words = content.split()
unique_words = set(words)

print("Frequency of each word : ")
for word in unique_words:
	if(word != "\n" and word != " "):
		print("\tFrequency of",word.ljust(6),"is : ",words.count(word))