# Introduction to Pandas

# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a Python dictionary
data = {
    "Voornaam"  : ["Alan", "Kevin", "Diane", "Patricia"],
    "Achternaam": ["Robinson", "O'Brien", "Cooper", "O'Connor"],
    "Geslacht"  : ["M", "M", "V", "V"],
    "Vermogen"  : [3200, 2750, 3425, 3820]
}

print(data)

# Create the DataFrame
df = pd.DataFrame(data)
print(df)

# An index column is automatically added by Pandas. This is to keep
#  track of rows and for fast manipulation of data by easy slicing.
#  Individual rows can be accessed by the index.

# Show the 4th case by row
print(df.loc[3])
print(df.loc[2:4])

# Show the column by name
print(df["Voornaam"])
print(df["Voornaam"].values)
print(df["Voornaam"].tolist())

# Summary
print(df.info())

# Get the list of columns
print(df.columns)
print(type(df.columns))
print(df.columns.tolist())
print(type(df.columns.tolist()))

# Get the index
print(df.index)

# Sneak peek
print(df.head())
print(df.head(1))
print(df.tail(2))

# Summary statistics (of numeric columns)
print(df.describe())
print(df.describe().index)
print(df.describe().loc["25%"])

# Number of rows in a DataFrame
print(len(df))
print(len(df["Voornaam"]))

# Looking up details about a DataFrame
print(dir(df))
print(help(df.loc))
