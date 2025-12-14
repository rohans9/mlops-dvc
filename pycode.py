import pandas as pd
import os

# df = pd.read_csv('C:\\Users\\Rohan Sahu\\MLOps\\people-1000.csv')
# print(df.head())
df = pd.read_csv("C:\\Users\\Rohan Sahu\\MLOps\\data\\people-1000.csv")

df = df.head(100)
data_dir = 'data'
# os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'people-1000.csv')
df.to_csv(file_path, index=False)
print(f"File saved to {file_path}")