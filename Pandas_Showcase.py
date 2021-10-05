# Introduction to Pandas

# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import time

Weather = pd.read_csv("https://raw.githubusercontent.com/PyDataWorkshop/datasets/master/weather_2012.csv")
Weather.info()

# EDA: Exploratory Data Analysis
print(Weather.head())
print(Weather.tail())

print(Weather["Weather"].unique())
print(len(Weather["Weather"].unique()))

print(Weather["Weather"].str.contains("Rain"))
print(Weather["Weather"].str.contains("Fog"))
print(Weather["Weather"].str.contains("Fog").mean())
print(Weather["Weather"].str.contains("Clear").mean())
print(Weather["Weather"].str.contains("Rain").mean())
print(Weather["Weather"].str.contains("Rain").head(5))

# Logical / boolean indexing to the main variable
print(Weather["Weather"][Weather["Weather"].str.contains("Rain")])
print(Weather["Weather"][Weather["Weather"].str.contains("Rain")].head(1))
# Find only "Rain" weather reports
print(Weather["Weather"][Weather["Weather"].str.contains("Rain")].unique())

# Find the rows that has weather value as "Fog"
print(Weather[Weather["Weather"] == "Fog"])

# Find rows where temperature is more than 10 degrees Celsius (C)
result = Weather[(Weather["Temp (C)"] > 10.0) & (Weather["Weather"].isin(["Cloudy", "Clear"]))]
print(result)
print(result[["Weather"]].shape)

# Group by on "Weather" column and count the number of records for each category
weather_grpby = Weather.groupby("Weather")["Dew Point Temp (C)"].count()
print(weather_grpby)
weather_grpby = Weather.groupby("Weather")["Dew Point Temp (C)"].mean()
print(weather_grpby)

# Group by on "Weather" column and count the number of records for each category
weather_grpby = Weather.groupby("Weather", as_index=False)["Dew Point Temp (C)"].count()
print(weather_grpby)

# Plot a line graph for "Temp (C)" field
# Plot function by default creates a "line" graph.
# The figure size si set for (width, height) in inches
print(Weather["Temp (C)"].plot(figsize=(17, 8)))
plt.show()
time.sleep(10)

# Use the groupby result from earlier to find the weather with the highest number of
weather_grpby.plot(kind="bar", figsize=(17, 8))
plt.show()
