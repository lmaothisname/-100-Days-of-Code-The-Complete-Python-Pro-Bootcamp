import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
# show the first 5 rows of our dataframe. 
print(df.head())
# To see the number of rows and columns we can use the shape attribute: 
print(df.shape)
# We can access the column names directly with the columns attribute. 
print(df.columns)
# we should try and figure out if there are any missing or junk data in our dataframe
# NAN values are blank cells or cells that contain strings instead of numbers.
# Use the .isna() method
print(df.isna())
# Check the last couple of rows in the dataframe
print(df.tail())
# There's two ways you can go about removing this row. The first way is to manually remove the row at index 50.
# The second way is to simply use the .dropna() method from pandas.
clean_df = df.dropna()
print(clean_df.tail())
# To access a particular column from a data frame we can use the square bracket notation
print(clean_df['Starting Median Salary'])
# To find the highest starting salary we can simply chain the .max() method. 
print(clean_df['Starting Median Salary'].max())
# the .idxmax() method will give us index for the row with the largest value. 
print(clean_df['Starting Median Salary'].idxmax())
# To see the name of the major that corresponds to that particular row, we can use the .loc (location) property. 
print(clean_df['Undergraduate Major'].loc[43])
# another way have the same thing
print(clean_df['Undergraduate Major'][43])
# If you don't specify a particular column you can use the .loc property to retrieve an entire row
print(clean_df.loc[43])

# challenge
# What college major has the highest mid-career salary?
# How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience). 
print(clean_df['Mid-Career Median Salary'].idxmax())
print(clean_df.loc[8])
# Which college major has the lowest starting salary and how much do graduates earn after university?
print(clean_df['Starting Median Salary'].idxmin())
print(clean_df.loc[49])
# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? 
print(clean_df['Mid-Career Median Salary'].idxmin())
print(clean_df.loc[18])

# How would we calculate the difference between the earnings of the 10th and 90th percentile?
# Well, Pandas allows us to do simple arithmetic with entire columns,
# so all we need to do is take the difference between the two columns
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
# Alternatively, you can also use the .subtract() method.
# clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])


# The output of this computation will be another Pandas dataframe column.
# We can add this to our existing dataframe with the .insert() method:
clean_df.insert(1,"Spread", spread_col)
print(clean_df.head())
# The first argument is the position of where the column should be inserted.
# In our case, it's at position 1, so the second column. 

# To see which degrees have the smallest spread, we can use the .sort_values() method
low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

# challenge 
# Using the .sort_values() method, can you find the degrees with the highest potential?
# Find the top 5 degrees with the highest values in the 90th percentile.  
high_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary",ascending=False)
print(high_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
print(f"The degrees with highest potential is: {high_potential['Undergraduate Major'][44]}")
highest_values_90th_percentile = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
print(f"The top 5 degrees with the highest values in the 90th percentile is \n{highest_values_90th_percentile[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()}")
# Also, find the degrees with the greatest spread in salaries.
# Which majors have the largest difference between high and low earners after graduation. 
greatest_spread = clean_df.sort_values("Spread",ascending=False)
print(print(greatest_spread[['Undergraduate Major', 'Spread']].head()))
highest_spread = clean_df.sort_values("Mid-Career Median Salary", ascending=False)
print(highest_spread[['Undergraduate Major', 'Mid-Career Median Salary']].head())

# Often times you will want to sum rows that belong to a particular category.
# To answer this question we need to learn to use the .groupby() 
print(clean_df.groupby("Group").count())
# use the .mean() method to find the average salary by group
pd.options.display.float_format = '{:,.2f}'.format 
print(clean_df.groupby("Group").mean(numeric_only=True))