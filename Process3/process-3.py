import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm


original_df = pd.read_csv("/content/drive/MyDrive/data/data-challenge-original.csv")
protected_df = pd.read_csv("/content/drive/MyDrive/data/protected_data_challenge.csv")

features = ['Age', 'Dependents', 'Income',
            'Rent', 'Loan_Repayment', 'Insurance', 'Groceries']

scaler = StandardScaler()
original_scaled = scaler.fit_transform(original_df[features])
protected_scaled = scaler.transform(protected_df[features])

# Create a similarity matrix using Euclidean distance
from scipy.spatial.distance import cdist
distances = cdist(protected_scaled, original_scaled, metric='euclidean')

matches = distances.argmin(axis=1)

decoded_df = protected_df.copy()
decoded_df['Decoded_Name'] = original_df.loc[matches, 'Name'].values
decoded_df['Decoded_Identifier'] = original_df.loc[matches, 'Identifier'].values

decoded_df.to_csv("decoded_data.csv", index=False)
