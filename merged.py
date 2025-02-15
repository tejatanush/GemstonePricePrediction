import pandas as pd

# Load both CSV files
df1 = pd.read_csv(r"C:\Users\tejat\Downloads\train (2).csv")
df2 = pd.read_csv(r"C:\Users\tejat\Downloads\test (1).csv")

# Concatenate both files
raw_df = pd.concat([df1,df2], ignore_index=True)

# Sort the merged data based on the 'id' column
raw_df = raw_df.sort_values(by='id', ascending=True)  # Sorts in ascending order

# Save the final sorted dataset as a new CSV file
raw_df.to_csv('raw.csv', index=False)

print("Merged and sorted train and test data into raw.csv successfully!")