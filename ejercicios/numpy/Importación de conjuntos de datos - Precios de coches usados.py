import pandas as pd
import numpy as np

# Data Acquisition

file_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'


# Read Data
df = pd.read_csv(file_path, header=None)

print("The first 5 rows of the dataframe") 
print(df.head(5))

# Question #1: 
# Check the bottom 10 rows of data frame "df".

print("\n Question #1 The last 10 rows of the dataframe \n")

print(df.tail(10))

## Add Headers
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

#  Replace headers and recheck our data frame:
df.columns = headers
df.columns

print("The first 10 rows of the dataframe")
df.head(10)

# Now, we need to replace the "?" symbol with NaN so the dropna() can remove the missing values:

df1=df.replace('?',np.nan)

# You can drop missing values along the column "price" as follows:

df=df1.dropna(subset=["price"], axis=0)

print(df.head(20))

# Question #2: 
# Find the name of the columns of the dataframe.


print("\n Question #2 The name of the columns of the dataframe \n")
print(df.columns)

# Save Dataset¶

print("\n Save Dataset \n")
df.to_csv("automobile.csv", index=False)

'''
Basic Insights from the Data set
After reading data into Pandas dataframe, it is time for you to explore the data set.

There are several ways to obtain essential insights of the data to help you better understand it.
'''

# Data Types

print("\n Data Types \n")
print(df.dtypes)

# Describe

print("example use describe")
print(df.describe())

print("example use describe all")
print(df.describe(include = "all"))

'''
Question #3: ¶
You can select the columns of a dataframe by indicating the name of each column. For example, you can select the three columns as follows:

dataframe[[' column 1 ',column 2', 'column 3']]

Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:

dataframe[[' column 1 ',column 2', 'column 3'] ].describe()

Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.
'''

print("\n Question #3 The describe method to the columns 'length' and 'compression-ratio' \n")
print(df[['length', 'compression-ratio']].describe())


'''
Info
You can also use another method to check your data set:
'''
print("\n Info \n")
print(df.info())


