import pandas as pd

# Create a pandas dataframe with 3 columns and 5 rows
df = pd.DataFrame({
    'Column1': [1, 2, 3, 4, 5],
    'Column2': ['A', 'B', 'C', 'D', 'E'],
    'Column3': [10.5, 20.3, 15.7, 25.1, 30.9]
})

print(df)
