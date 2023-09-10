#To find the percentinle informations of speed and alerts 
import pandas as pd
df = pd.read_csv('D:/Desktop/Intel/revised_dataset_updated.csv')
speed_25th_percentile = df['speed'].quantile(0.25)
speed_50th_percentile = df['speed'].quantile(0.50)
speed_75th_percentile = df['speed'].quantile(0.75)
print(f"The speed below which 25% of alerts occur is: {speed_25th_percentile} km/h")
print(f"The speed below which 25% of alerts occur is: {speed_50th_percentile} km/h")
print(f"The speed below which 25% of alerts occur is: {speed_75th_percentile} km/h")

#To find Black Spots 
import pandas as pd
dataset = pd.read_csv('D:/Desktop/Intel/revised_dataset_updated.csv')
location_alert_type_counts = dataset.groupby(['lat', 'long', 'alert']).size()
top_black_spots = location_alert_type_counts.groupby(['lat', 'long']).sum().nlargest(10)
print("Top 10 Black Spots:")
print(top_black_spots)
for index, count in top_black_spots.iteritems():
    latitude, longitude = index
    alerts_in_black_spot = dataset[(dataset['lat'] == latitude) & (dataset['long'] == longitude)]
    most_common_alert = alerts_in_black_spot['alert'].value_counts().idxmax()
    print(f"Black Spot (Latitude: {latitude}, Longitude: {longitude}, Alert Count: {count})")
    print(f"Most Common Alert: {most_common_alert}")
    print()


#Most Common Alerts for Each Vehicle
import pandas as pd
dataset = pd.read_csv('D:/Desktop/Intel/revised_dataset_updated.csv')
vehicle_alert_counts = dataset.groupby(['vehicle', 'alert']).size().unstack(fill_value=0)
most_common_alerts = vehicle_alert_counts.idxmax(axis=1)
print("Most Common Alerts for Each Vehicle:")
print(most_common_alerts)



#To find the peak hours of each alerts
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('D:/Desktop/Intel/revised_dataset_updated.csv')
dataset['time'] = pd.to_datetime(dataset['time'])
dataset['hour'] = dataset['time'].dt.hour
alerts_by_hour_type = dataset.groupby(['hour', 'alert']).size().unstack(fill_value=0)
peak_hours = alerts_by_hour_type.sum().idxmax()
plt.figure(figsize=(10, 6))
for alert_type in alerts_by_hour_type.columns:
    alerts_by_hour_type[alert_type].plot(label=alert_type)
plt.xlabel("Hour")
plt.ylabel("Number of Alerts")
plt.title("Alert Distribution in Peak Hour(s)")
plt.xticks(range(24))
plt.legend()
plt.tight_layout()
plt.show()


#Variation of Alert Type with Mean Speed
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataset = pd.read_csv('D:/Desktop/Intel/revised_dataset_updated.csv')
mean_speed_by_alert = dataset.groupby('alert')['speed'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=mean_speed_by_alert, x='alert', y='speed', marker='o')
plt.xlabel('Alert Type')
plt.ylabel('Mean Speed (km/h)')
plt.title('Variation of Alert Type with Mean Speed')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
