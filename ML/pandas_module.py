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


    #advanced pandas operations
    # Grouping
    grouped = df.groupby('Age').size()
    print("Grouped DataFrame:\n", grouped)  
    # Merging
    df2 = create_dataframe([['David', 40], ['Eve', 22]], columns=['Name', 'Age'])
    merged = pd.concat([df, df2])
    print("Merged DataFrame:\n", merged)
    # Handling missing data 
    df3 = create_dataframe([['Frank', 28], ['Grace', None]], columns=['Name', 'Age'])
    print("DataFrame with missing data:\n", df3)
    print("Fill missing data:\n", df3.fillna({'Age': df3['Age'].mean()}))
    print("Drop rows with missing data:\n", df3.dropna())
    # Handling duplicates
    df4 = create_dataframe([['Alice', 30], ['Bob', 25], ['Alice', 30]], columns=['Name', 'Age'])
    print("DataFrame with duplicates:\n", df4)
    print("Drop duplicates:\n", df4.drop_duplicates())
    # Handling outliers
    df5 = create_dataframe([['Alice', 30], ['Bob', 25], ['Charlie', 350]], columns=['Name', 'Age'])
    print("DataFrame with outlier:\n", df5)
    z_scores = (df5['Age'] - df5['Age'].mean()) / df5['Age'].std()
    print("DataFrame without outlier:\n", df5[np.abs(z_scores) < 3])    
    # Handling categorical data 
    df6 = create_dataframe([['Alice', 'Female'], ['Bob', 'Male'], ['Charlie', 'Male']], columns=['Name', 'Gender'])
    print("DataFrame with categorical data:\n", df6)
    df6['Gender'] = df6['Gender'].astype('category')
    print("DataFrame with categorical data:\n", df6)        
    # Handling time series data
    df7 = create_dataframe([['2023-01-01', 100], ['2023-01-02', 120], ['2023-01-03', 110]], columns=['Date', 'Value'])
    df7['Date'] = pd.to_datetime(df7['Date'])   
    df7.set_index('Date', inplace=True)
    print("DataFrame with time series data:\n", df7)
    resampled = df7.resample('D').mean()
    print("Resampled DataFrame:\n", resampled)
    # Handling text data
    df8 = create_dataframe([['Alice', 'Hello World'], ['Bob', 'Pandas is great'], ['Charlie', 'Data Science']], columns=['Name', 'Text'])
    print("DataFrame with text data:\n", df8)
    df8['Text'] = df8['Text'].str.lower()
    print("DataFrame with lower case text:\n", df8)
    df8['Text'] = df8['Text'].str.replace('[^\w\s]', '')
    print("DataFrame with removed punctuation:\n", df8)
    # Handling JSON data    
    json_data = [
        {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
    ]
    df9 = create_dataframe(json_data, columns=['Name', 'Age', 'City'])
    print("DataFrame with JSON data:\n", df9)
    # Handling binary data  
    binary_data = [
        {'Name': 'Alice', 'Data': b'\x00\x01\x02'},
        {'Name': 'Bob', 'Data': b'\x03\x04\x05'},
        {'Name': 'Charlie', 'Data': b'\x06\x07\x08'}
    ]
    df10 = create_dataframe(binary_data, columns=['Name', 'Data'])
    print("DataFrame with binary data:\n", df10)
    # Handling missing data in binary data
    df10.loc[1, 'Data'] = None
    print("DataFrame with missing binary data:\n", df10)
    print("Drop rows with missing binary data:\n", df10.dropna())
    
    # Handling missing data in time series data
    df7.loc['2023-01-02', 'Value'] = None
    print("DataFrame with missing time series data:\n", df7)
    print("Fill missing time series data:\n", df7.fillna(method='ffill'))
    print("Drop rows with missing time series data:\n", df7.dropna())
    # Handling missing data in text data
    df8.loc[1, 'Text'] = None
    print("DataFrame with missing text data:\n", df8)
    print("Drop rows with missing text data:\n", df8.dropna())
    # Handling missing data in categorical data 
    df6.loc[2, 'Gender'] = None
    print("DataFrame with missing categorical data:\n", df6)
    print("Drop rows with missing categorical data:\n", df6.dropna())
    # Handling missing data in JSON data        
    df9.loc[1, 'Age'] = None
    print("DataFrame with missing JSON data:\n", df9)
    print("Drop rows with missing JSON data:\n", df9.dropna())
    # Handling missing data in binary data  
    df10.loc[2, 'Data'] = None
    print("DataFrame with missing binary data:\n", df10)
    print("Drop rows with missing binary data:\n", df10.dropna())
    # Handling missing data in time series data
    df7.loc['2023-01-02', 'Value'] = None
    print("DataFrame with missing time series data:\n", df7)
    print("Fill missing time series data:\n", df7.fillna(method='ffill'))
    print("Drop rows with missing time series data:\n", df7.dropna())
    # Handling missing data in text data
    df8.loc[1, 'Text'] = None
    print("DataFrame with missing text data:\n", df8)
    print("Drop rows with missing text data:\n", df8.dropna())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    # Handling missing data in categorical data
    df6.loc[2, 'Gender'] = None
    print("DataFrame with missing categorical data:\n", df6)    
    print("Drop rows with missing categorical data:\n", df6.dropna())
    # Handling missing data in JSON data
    

# Run the demonstration
if __name__ == "__main__":
    dataframe_operations()