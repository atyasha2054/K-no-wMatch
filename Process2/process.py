import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist


original_df = pd.read_csv("/content/drive/MyDrive/data/data-challenge-original.csv")
protected_df = pd.read_csv("/content/drive/MyDrive/data/protected_data_challenge.csv")

exclude_cols = ['Name', 'Identifier']
common_cols = list(set(original_df.columns).intersection(set(protected_df.columns)))
numeric_cols = [col for col in common_cols if col not in exclude_cols and np.issubdtype(original_df[col].dtype, np.number)]

# Step 3: Feature Weighting
feature_weights = {
    'Income': 2.0, 'Groceries': 1.8, 'Rent': 1.5,
    'Loan_Repayment': 1.5, 'Insurance': 1.3,
    'Age': 1.0, 'Occupation': 1.0, 'City_Tier': 1.0,
    'Dependents': 1.0
}
weights = np.array([feature_weights.get(col, 1.0) for col in numeric_cols])

# Step 4: Standardization + Weighting
scaler = StandardScaler()
original_scaled = scaler.fit_transform(original_df[numeric_cols])
protected_scaled = scaler.transform(protected_df[numeric_cols])
original_weighted = original_scaled * weights
protected_weighted = protected_scaled * weights

# Step 5: Dimensionality Reduction using PCA
pca = PCA(n_components=0.95)
original_pca = pca.fit_transform(original_weighted)
protected_pca = pca.transform(protected_weighted)

# Step 6: Efficient Matching in Batches
def batched_matching(protected_data, original_data, batch_size=1000):
    matched_indices = []
    for i in range(0, protected_data.shape[0], batch_size):
        batch = protected_data[i:i+batch_size]
        dists = cdist(batch, original_data, metric='euclidean')
        batch_indices = np.argmin(dists, axis=1)
        matched_indices.extend(batch_indices)
    return matched_indices

matched_indices = batched_matching(protected_pca, original_pca)

# Step 7: Reconstruct Matched DataFrame
protected_df['Matched_Index'] = matched_indices
matched_original_rows = original_df.iloc[matched_indices].reset_index(drop=True)
match_results = pd.concat([protected_df.reset_index(drop=True), matched_original_rows.add_prefix("Original_")], axis=1)

# Step 8: Save Final Results
match_results.to_csv("match_results.csv", index=False)
print("Matching complete. Results saved in match_results.csv.")
