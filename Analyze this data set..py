import pandas as pd

# Load the data set into a pandas dataframe
df = pd.read_csv("/content/1. WeatherData.csv")

# Find all the unique 'Wind Speed' values in the data
unique_wind_speed = df['Wind Speed_km/h'].unique()
print("Unique Wind Speed:", unique_wind_speed)

# Find the number of times when the 'Weather is exactly Clear'
clear_weather_count = df[df['Weather'] == 'Clear'].shape[0]
print("Clear Weather Count:", clear_weather_count)

# Find the number of times when the 'Wind Speed was exactly 4 km/h'
wind_speed_4_count = df[df['Wind Speed_km/h'] == 4].shape[0]
print("Wind Speed 4 Count:", wind_speed_4_count)

# Rename the column name 'Weather' of the dataframe' to 'Weather Condition'
df.rename(columns={'Weather': 'Weather Condition'}, inplace=True)

# What is the Variance of 'Relative Humidity' in this data
rel_humidity_var = df['Rel Hum_%'].var()
print("Relative Humidity Variance:", rel_humidity_var)

# Find out all the Null Values in the data
null_values = df.isnull().sum()
print("Null Values:\n", null_values)

# What is the mean 'Visibility'
visibility_mean = df['Visibility_km'].mean()
print("Visibility Mean:", visibility_mean)

# Find all instances when 'Snow' was recorded
snow_rows = df[df['Weather Condition'] == 'Snow']
print("Snow Rows:\n", snow_rows)

# Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'
above_24_and_25 = df[(df['Wind Speed_km/h'] > 24) & (df['Visibility_km'] == 25)]
print("Wind Speed above 24 and Visibility 25:\n", above_24_and_25)

# What is the Mean value of each column against each Weather condition
mean_by_weather = df.groupby(by='Weather Condition').mean()
print("Mean by Weather:\n", mean_by_weather)

# What is the Minimum & Maximum value of each column against each weather condition
min_max_by_weather = df.groupby(by='Weather Condition').agg(['min', 'max'])
print("Min Max by Weather:\n", min_max_by_weather)

# Find all instances when 'Weather is Clear' or 'Visibility' is above 40
clear_or_visibility_above_40 = df[(df['Weather Condition'] == 'Clear') | (df['Visibility_km'] > 40)]
print("Clear or Visibility above 40:\n", clear_or_visibility_above_40)