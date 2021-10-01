import pandas as pd
import matplotlib.pyplot as plt

devices, users, usage = pd.read_csv("./sample_data/device_data.csv"), pd.read_csv("./sample_data/user_data.csv"), pd.read_csv("./sample_data/usage_data.csv")
result = pd.merge(usage, users[['use_id', 'platform', 'device']], on='use_id', how='left')
devices.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result, devices[['manufacturer', 'Model']], left_on='device', right_on='Model', how='left')
result["total_usage"] = result.iloc[:, :2].sum(axis=1)

printData = pd.DataFrame(result.groupby("manufacturer").agg({
    "outgoing_mins_per_month": "sum",
    "outgoing_sms_per_month": "sum",
    "monthly_mb": "sum",
    "total_usage": "sum"
}))

printData.plot(kind='bar', subplots=True, layout=(2, 2))
plt.tight_layout()
plt.show()