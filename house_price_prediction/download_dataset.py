import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download("yasserh/housing-prices-dataset")

print("Path to dataset files:", path)
