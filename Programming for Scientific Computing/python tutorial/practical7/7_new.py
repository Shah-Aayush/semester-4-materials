#!/usr/bin/env python3

# Develop a python program that reads the data from a given CSV file, which is having phone usage data using a different branded mobile phone. Determine if the usage patterns for users differ between different devices. For example, do users using Samsung devices use more call minutes than those using LG devices?

import matplotlib.pyplot as plt
import pandas as pd

# Reading a comma-separated values (csv) file
user_data = pd.read_csv("./sample_data/user_data.csv")
devices_data = pd.read_csv("./sample_data/device_data.csv")
usage_data = pd.read_csv("./sample_data/usage_data.csv")

result_data = pd.merge(usage_data, user_data[['use_id','platform','device']], on='use_id', how='left')		# on='use_id' : Column (here, use_id) or index level names to join on. || how='left' : use only keys from left frame, similar to a SQL left outer join; preserve key order.
devices_data.rename(columns={"Retail Branding":"Manufacturer"}, inplace=True)		# inplace : Whether to return a new DataFrame.
result_data = pd.merge(result_data, devices_data[['Manufacturer','Model']], left_on='device', right_on='Model', how='left')		# left_on : Column or index level names to join on in the left DataFrame.
#print(result_data)
result_data['total_usage'] = result_data.iloc[:, :2].sum(axis=1)

final_data = pd.DataFrame(result_data.groupby("Manufacturer").agg({
	"outgoing_mins_per_month": "sum",
	"outgoing_sms_per_month" : "sum",
	"monthly_mb": "sum",
	"total_usage": "sum"
}))

final_data.plot(kind='bar', subplots=True, layout=(2,2))
plt.tight_layout()		# automatically adjusts subplot params so that the subplots fits in to the figure area.
plt.show()