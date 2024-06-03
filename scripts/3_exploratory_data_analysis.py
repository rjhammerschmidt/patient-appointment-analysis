# Exploratory Data Analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('../data/appointments_cleaned.csv')

# Plot the distribution of age
sns.histplot(df['Age'], bins=30)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('../visualizations/age_distribution.png')
plt.show()

# No-show rate
no_show_rate = df['No-show'].value_counts(normalize=True)
print(no_show_rate)

# Plot no-show rate
sns.barplot(x=no_show_rate.index, y=no_show_rate.values)
plt.title('No-show Rate')
plt.xlabel('No-show')
plt.ylabel('Proportion')
plt.savefig('../visualizations/no_show_rate.png')
plt.show()

# No-show rate by Gender
sns.catplot(x='Gender', y='No-show', data=df, kind='bar')
plt.title('Impact of Gender on No-show Rate')
plt.xlabel('Gender')
plt.ylabel('No-show Rate')
plt.gca().invert_yaxis()
plt.savefig('../visualizations/gender_no_show_rate.png')
plt.show()

# No-show rate by Weekday
df['AppointmentDayOfWeek'] = pd.to_datetime(df['AppointmentDay']).dt.day_name()

# Plot no-show rate by weekday
sns.catplot(x='AppointmentDayOfWeek', y='No-show', data=df, kind='bar')
plt.title('No-show Rate by Weekday')
plt.xlabel('Weekday')
plt.ylabel('No-show Rate')
plt.gca().invert_yaxis()
plt.xticks(rotation=45)
plt.savefig('../visualizations/weekday_no_show_rate.png')
plt.show()
