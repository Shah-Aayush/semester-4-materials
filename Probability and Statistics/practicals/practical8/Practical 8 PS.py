#!/usr/bin/env python
# coding: utf-8

# In[1]:




n=int(input('Enter total number of sentences :'))
st=[]           #list of sentences
sentiment=[]    #list of sentiments of sentences
final=[]        #list of all the words of sentences
positive=[]     #list of all words in positive sentences
temp=[]         #temporary list

def fact(num):
    f=1
    for i in (1,num+1):
        f*=i
    return f
    

for i in range(0,n):
    
    st.append(input(f'Enter sentence number {i+1} : '))
    while(not st[i].islower()):                                              #this loop will take care that user gives valid input 
        
        print('Invalid Statement.Enter only in lower case.')
        st[i]=input(f'Enter sentence number {i+1} : ')
        
    temp=st[i].split()                                                        #to get all words of the sentences
    for j in temp:
        final.append(j)                                                       #inserting all word of the sentence in final list
    
    sentiment.append(input('Enter the sentiment of this sentence (p for positive and n for negative) : '))
    if(not(sentiment[i]=="p" or sentiment[i]=="P" or sentiment[i]=="n" or sentiment[i]=="N")):    #this loop will take care that user gives valid input
        print('Invalid Sentiment')
        sent[i]=input('Enter the sentiment of this sentence (p for positive and n for negative) : ')
        

temp2=[]
for i in range(0,n):
    if(sentiment[i]=='p' or sentiment[i]=='P'):
        temp2=st[i].split()
        for j in temp2:
            positive.append(j)
            
a=input("enter a:")
while a not in final:
    print('Not a valid word.Enter a word which is already there in statements')
    a=input()
    
b=input("enter b:")
while b not in final:
    print('Not a valid word.Enter a word which is already there in statements')
    b=input()
    
c=input("enter c:")    
while c not in final:
    print('Not a valid word.Enter a word which is already there in statements')
    c=input()

d=input("enter d:")
while d not in final:
    print('Not a valid word.Enter a word which is already there in statements')
    d=input()

e=input("enter e:")
while e not in final:
    print('Not a valid word.Enter a word which is already there in statements')
    e=input()

pa=positive.count(a)/len(positive)
pb=positive.count(b)/len(positive)
pc=positive.count(c)/len(positive)
pd=positive.count(d)/len(positive)
pe=positive.count(e)/len(positive)

print(pa,pb,pc,pd,pe)

p=fact(len(positive))/(fact(positive.count(a))*fact(positive.count(b))*fact(positive.count(c))*fact(positive.count(d))*fact(positive.count(e)))
print(p)
p*=((pa**positive.count(a))*(pb**positive.count(b))*(pc**positive.count(c))*(pd**positive.count(d))*(pe**positive.count(e)))

print(positive)

print("joint probabilty:",p)


# In[ ]:




