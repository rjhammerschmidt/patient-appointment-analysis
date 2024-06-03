# Data Cleaning
import pandas as pd

# Load the dataset
df = pd.read_csv('../data/appointments.csv')

# Check for missing values
print(df.isnull().sum())

# Fill missing values or drop rows/columns if necessary
df.dropna(inplace=True)

# Convert columns to appropriate data types
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Save the cleaned dataset
df.to_csv('../data/appointments_cleaned.csv', index=False)
