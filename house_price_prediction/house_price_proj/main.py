import pandas as pd
import os

# Corrected dataset path
dataset_path = r"C:\Users\MILLY\.cache\kagglehub\datasets\yasserh\housing-prices-dataset\versions\1\housing.csv"

# Load the dataset
df = pd.read_csv(dataset_path)

# Show the first few rows
print("Dataset loaded successfully.")
print(df.head())
