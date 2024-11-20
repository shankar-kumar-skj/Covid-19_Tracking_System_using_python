
import pandas as pandas

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pandas.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print("\nAverage Age:", average_age)

# Filter rows where Age is greater than 28
filtered_df = df[df['Age'] > 28]
print("\nFiltered DataFrame (Age > 28):")
print(filtered_df)