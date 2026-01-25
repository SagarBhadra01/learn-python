import pandas as pd
import numpy as np
""" With Pandas, you can perform a wide range of data manipulation and analysis tasks, including:
Creating and manipulating DataFrames and Series.
"""

def create_dataframe(data, columns=None):
    """Create a Pandas DataFrame from the given data with optional column names."""
    return pd.DataFrame(data, columns=columns)

def dataframe_operations():
    """Demonstrate basic Pandas DataFrame operations."""
    df = create_dataframe([['Alice', 30], ['Bob', 25], ['Charlie', 35]], columns=['Name', 'Age'])
    print("DataFrame:\n", df)

    # Basic operations
    print("DataFrame Info:")
    print(df.info())
    print("DataFrame Description:")
    print(df.describe())
    print("DataFrame Head:")
    print(df.head())
    print("DataFrame Tail:")
    print(df.tail())
    print("DataFrame Columns:")
    print(df.columns)
    print("DataFrame Index:")
    print(df.index)
    print("DataFrame Values:\n", df.values)
    print("DataFrame Shape:", df.shape)
    # Selection
    print("Select 'Name' column:\n", df['Name'])
    print("Select rows 1 and 2:\n", df[1:3])
    # Filtering
    print("Filter Age > 28:\n", df[df['Age'] > 28])
    # Sorting
    print("Sort by Age:\n", df.sort_values(by='Age'))
    # Aggregation
    print("Average Age:", df['Age'].mean())
    print("Max Age:", df['Age'].max())
    print("Min Age:", df['Age'].min())
    # Adding a new column
    df['Age in 5 Years'] = df['Age'] + 5    
    print("DataFrame with new column:\n", df)
    

# Run the demonstration
if __name__ == "__main__":
    dataframe_operations()