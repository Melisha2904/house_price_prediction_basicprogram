# house_price_prediction_basic_program
This project uses machine learning techniques to predict house prices using a Kaggle dataset.

Requirements
Python 3.12+

Install dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
Dependencies:

pandas

seaborn

matplotlib

scikit-learn

kagglehub

Setup
Install Python and Dependencies:
pip install pandas seaborn matplotlib scikit-learn kagglehub
Download the Dataset:

The dataset is automatically downloaded using kagglehub:
import kagglehub

# Download dataset
path = kagglehub.dataset_download("yasserh/housing-prices-dataset")
print("Dataset path:", path)
Update Dataset Path:
Update the path in main.py to match where the dataset is downloaded:
dataset_path = r"C:\Users\MILLY\.cache\kagglehub\datasets\yasserh\housing-prices-dataset\versions\1\housing.csv"
Run the Script:
python house_price_proj/main.py
Project Workflow
Download and Load Dataset

Data Exploration & Preprocessing

Model Training & Evaluation (Linear Regression)

Save Trained Model

Example Output
Dataset loaded successfully.
Mean Absolute Error: 25000.54
Mean Squared Error: 850000000.0
Model saved as 'house_price_model.pkl'
