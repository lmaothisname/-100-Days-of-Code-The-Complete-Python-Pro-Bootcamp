import pandas as pd
import matplotlib.pyplot as plt

# Challenge: Read the .csv file and store it in a Pandas dataframe
columns_names = ['DATE', 'TAG', 'POSTS']
df = pd.read_csv("QueryResults.csv", names=columns_names, header=0)

# Challenge: Examine the first 5 rows and the last 5 rows of the of the dataframe
print(df.head())
print(df.tail())

# Challenge: Check how many rows and how many columns there are. What are the dimensions of the dataframe?
print(df.shape)

# Challenge: Count the number of entries in each column of the dataframe
print(df.count())

# Challenge: Calculate the total number of post per language. Which Programming language has had the highest total number of posts of all time?
df_total_posts_per_language = df.groupby('TAG').sum()
print(df_total_posts_per_language)
max_months_language = df_total_posts_per_language['POSTS'].idxmax()
max_months_count = df_total_posts_per_language['POSTS'].max()
print(f"The language with the highest total number of posts of all time is '{max_months_language}' with {max_months_count} posts.")

# Challenge: How many months of data exist per language? Which language had the fewest months with an entry? 
df_months_per_language = df.groupby('TAG').count()
print(df_months_per_language)
min_months_language = df_months_per_language["DATE"].idxmin()
min_months_count = df_months_per_language["DATE"].min()

print(f"The language with the fewest months of data is '{min_months_language}' with {min_months_count} months.")
# Selecting an Individual Cell
print(df['DATE'][1])
# Alternative ways
print(df.DATE[1])

# Pandas can help us convert the string to a timestamp using the to_datetime() method. 
df.DATE = pd.to_datetime(df.DATE)
print(df.head())
# Sometimes you want to convert your DataFrame so that each category has its own column
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)

# The easiest way to accomplish this is by using the .pivot() method in Pandas
pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

# Challenge: pivot the df DataFrame so that each row is a date and each column is a programming language? Store the result under a variable called reshaped_df.  
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
print(reshaped_df)

# Challenge: What are the dimensions of our new dataframe?
# How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.
print(reshaped_df.shape)
print(reshaped_df.columns)
print(reshaped_df.head())

# Challenge: Count the number of entries per programming language. Why might the number of entries be different? 
print(reshaped_df.count())
# When we count the number of entries per column we see that not all languages are the same. The reason is that the .count() method excludes NaN values.
# When we pivoted the DataFrame the NaN values were inserted when there were no posts for a language in that month (e.g., Swift in July, 2008). 

# Dealing with NaN Values, We can do this with the .fillna() method. 
reshaped_df.fillna(0, inplace=True)
print(reshaped_df.head())
# The inplace argument means that we are updating reshaped_df. Without this argument we would have to write something like this:
# reshaped_df = reshaped_df.fillna(0) 

# We can also check if there are any NaN values left in the entire DataFrame with this line:
print(reshaped_df.isna().values.any())
# This means we don't have to search through the entire DataFrame to spot if .isna() is True. 

# show a line chart for the popularity of a programming language se the .plot() in matplotlib library
print(plt.plot(reshaped_df.index, reshaped_df['java']))


## Styling the Chart
# .figure() - allows us to resize our chart

# .xticks() - configures our x-axis

# .yticks() - configures our y-axis

# .xlabel() - add text to the x-axis

# .ylabel() - add text to the y-axis

# .ylim() - allows us to set a lower and upper bound 

# To make our chart larger we can provide a width (16) and a height (10) as the figsize of the figure. 
plt.figure(figsize=(16,10))
print(plt.plot(reshaped_df.index,reshaped_df.java))

# when we increase the size of the chart,
# we should also increase the fontsize of the ticks on our axes so that they remain easy to read
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
print(plt.plot(reshaped_df.index,reshaped_df.java))

# we can add labels. we're never going to get less than 0 posts, so let's set a lower limit of 0 for the y-axis with .ylim()
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Date', fontsize=14)
plt.xlabel('Number of posts', fontsize=14)
plt.ylim(0,35000)
print(plt.plot(reshaped_df.index,reshaped_df.java))

# Challenge: Show two line (e.g. for Java and Python) on the same chart.
plt.figure(figsize=(16,10)) 
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of posts', fontsize=14)
plt.ylim(0,35000)
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)

#  to plot all the programming languages on the same chart use a for-loop
plt.figure(figsize=(16,10)) 
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in reshaped_df.columns:
  plt.plot(reshaped_df.index, reshaped_df[column])
# It's really hard to make out without a legend that tells us which colour corresponds to each language. 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], 
             linewidth=3, label=reshaped_df[column].name)
 
plt.legend(fontsize=16) 

# Smoothing out Time-Series Data
roll_df = reshaped_df.rolling(window=6).mean()
 
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], 
             linewidth=3, label=roll_df[column].name)
 
plt.legend(fontsize=16)

# Learning Points & Summary

    # used .groupby() to explore the number of posts and entries per programming language

    # converted strings to Datetime objects with to_datetime() for easier plotting

    # reshaped our DataFrame by converting categories to columns using .pivot()

    # used .count() and isna().values.any() to look for NaN values in our DataFrame, which we then replaced using .fillna()

    # created (multiple) line charts using .plot() with a for-loop

    # styled our charts by changing the size, the labels, and the upper and lower bounds of our axis.

    # added a legend to tell apart which line is which by colour

    # smoothed out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.

