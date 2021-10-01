#!/usr/bin/env python3

# Develop a python program that reads the data from a given CSV file, which is having phone usage data using a different branded mobile phone. Determine if the usage patterns for users differ between different devices. For example, do users using Samsung devices use more call minutes than those using LG devices?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./sample_data/data.csv')

#print(df.to_string())

motorola_users = list(pd.read_csv('./sample_data/data.csv', usecols =["Motorola"],squeeze = True))
lg_users = list(pd.read_csv('./sample_data/data.csv', usecols =["LG"],squeeze = True))
samsung_users = list(pd.read_csv('./sample_data/data.csv', usecols =["Samsung"],squeeze = True))
apple_users = list(pd.read_csv('./sample_data/data.csv', usecols =["Apple"],squeeze = True))

print(sum(motorola_users)/len(motorola_users))
print(sum(lg_users)/len(lg_users))
print(sum(samsung_users)/len(samsung_users))
print(sum(apple_users)/len(apple_users))

avg_motorola = sum(motorola_users)/len(motorola_users)
avg_lg = sum(lg_users)/len(lg_users)
avg_samsung = sum(samsung_users)/len(samsung_users)
avg_apple = sum(apple_users)/len(apple_users)

max_avg = max(avg_motorola,avg_lg,avg_samsung,avg_apple)

explod_pie = ()
#if max_avg==avg_motorola:
#	explod_pie = (0.2,0,0,0)
#elif max_avg==avg_lg:
#	explod_pie = (0,0.2,0,0)
#elif max_avg==avg_samsung:
#	explod_pie = (0,0,0.2,0)
#else:
#	explod_pie = (0,0,0,0.2)

if avg_samsung>avg_lg:
	explod_pie = (0,0.1,0.4,0)
	title_pie = "Samsung devices use more call minutes than LG"
elif avg_samsung<avg_lg:
	explod_pie = (0,0.4,0.1,0)
	title_pie = "LG devices use more call minutes than Samsung"
else:
	explod_pie = (0,0.2,0.2,0)
	title_pie = "Samsung and LG devices are using equally call minutes"

plt.pie([avg_motorola,avg_lg,avg_samsung,avg_apple],labels=['Motorola','LG','Samsung','Apple'], colors=['r','g','b','y','c'], startangle=90,shadow=True,explode=explod_pie,autopct ='%1.1f%%')
plt.title(title_pie)
plt.show()