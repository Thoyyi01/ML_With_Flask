import pandas as pd

# Define the data
data = {
    'Name': ['Alice', None, None, 'Charlie', 'Bob'],
    'Age': [25, 30, 45, None, 40],
    'City': ['Hyd', 'Ben', None, 'Kerala', None],
    'Gender': ['M', 'F', 'M', 'F', 'M']
}

# Create the DataFrame
df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:")
print(df)

# Fill missing values using mean, median, and mode
# Mean imputation
df_filled_mean = df.copy()
df_filled_mean['Age'].fillna(df['Age'].mean(), inplace=True)

# Median imputation
df_filled_median = df.copy()
df_filled_median['Age'].fillna(df['Age'].median(), inplace=True)

# Mode imputation (for categorical columns like Gender, City)
df_filled_mode = df.copy()
df_filled_mode['City'].fillna(df['City'].mode()[0], inplace=True)
df_filled_mode['Gender'].fillna(df['Gender'].mode()[0], inplace=True)

# Display results
print("\nDataFrame After Replacing Missing Values with Mean:")
print(df_filled_mean)

print("\nDataFrame After Replacing Missing Values with Median:")
print(df_filled_median)

print("\nDataFrame After Replacing Missing Values with Mode:")
print(df_filled_mode)


data = f
'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
'Age': [25, 30, 25, 35, 30],
'City': ['hyd', 'goa', 'banglore', 'hyd', 'chennai']
df = pd. DataFrame (data)
print("Original DataFrame:")
print(df)
# Identify duplicate rows
duplicates = df[df.duplicated()]
print("\nIdentified Duplicates: ")
print (duplicates)
# Remove duplicates, keeping the first occurrence
df_cleaned = df.drop_duplicates()
print("\nDataFrame After Removing Duplicates:")
printdf_cleaned)