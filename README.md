# 🔎 K(no)wMatch — Decode the Unknown, Match with Precision

> "Reconstructing hidden identities from anonymized data using precision-driven matching techniques."

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Numpy](https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Data Science](https://img.shields.io/badge/Data_Science-000000?style=for-the-badge&logo=data:image/png;base64,...)

---

## 🧠 Project Overview

**K(no)wMatch** is a powerful de-anonymization framework developed to **reconstruct hidden identities** from a **protected dataset**.

We leverage a suite of **advanced matching algorithms**, **feature weighting strategies**, and **ensemble techniques** to maximize decoding accuracy — carefully matching encrypted profiles to their original counterparts.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** — Data Processing
- **NumPy** — Numerical Computation
- **Scikit-Learn** — Scaling, PCA, OneHotEncoding
- **SciPy** — Distance Metrics
- **TQDM** — Progress Tracking
- **Matplotlib/Seaborn**  — Visualizations

---

## 🔥 Techniques Implemented

| Process | Description |
|:--------|:------------|
| **1️⃣ Cosine Similarity Matching** | Finding nearest neighbors using cosine similarity on normalized features. |
| **2️⃣ Batch-Based Matching (Memory Efficient)** | PCA-driven dimensionality reduction with batched Euclidean matching. |
| **3️⃣ Direct Euclidean Distance Matching** | Matching based purely on minimal Euclidean distance between feature vectors. |
| **4️⃣ Feature-Weighted Matching** | Customized weighting of features based on domain knowledge importance. |
| **5️⃣ Hybrid Top-3 Candidate Decoding** | Combining weighted and non-weighted scores for ultimate decoding accuracy. |

---

## ⚡ Final Solution Strategy

✅ Apply **Process 4** and **Process 5** separately on the protected data.  
✅ Merge the outputs containing **matching score** and **weighted matching score**.  
✅ Compute a **Final Hybrid Score**:
```
Final Score = 0.3 × Matching Score + 0.7 × Weighted Matching Score
```
✅ Select best match based on the **lowest Final Score**.  
✅ Implement **Top-3 Decoding** for validation and improved recall.

---

## 📈 Evaluation Metrics

| Metric | Result |
|:-------|:-------|
| Top-1 Accuracy | **92.1%** |
| Top-3 Recall | **98.5%** |
| Average Final Score | **0.243** |
| Score Standard Deviation | **0.065** |

**Note:**  
Higher weights on **critical fields** like `Income`, `Occupation`, and `Loan Repayment` significantly boosted reconstruction success rates.

---

## 🔄 Dataflow Pipeline

```plaintext
1. Load Datasets (Original + Protected)
          ↓
2. Feature Preprocessing (Scaling + Encoding + Weighting)
          ↓
3. Individual Matching (Cosine, Euclidean, Weighted Matching)
          ↓
4. Merge Match Results (Hybrid Score Calculation)
          ↓
5. Top-1 and Top-3 Match Selection
          ↓
6. Save Decoded Outputs
```

---

## ✨ **Key Highlights**
	•	Smart Feature Engineering: Domain-driven importance weighting.
	•	Top-K Matching: Provides Top-3 probable matches to ensure better validation.
	•	Robust against Noise: Scalable to datasets with slight anonymization perturbations.
	•	Memory Efficient: Batch-based matching capable of handling large-scale datasets.
	•	Reproducible Results: Fully documented pipeline with modular scripts.

---

## 🚀**Why Our Solution is the Best**

Our solution doesn’t rely on just one attack technique.
Instead, it creates an intelligent hybrid approach by:
	•	Combining unweighted and weighted distance metrics,
	•	Carefully tuning feature importances using domain knowledge,
	•	Using Top-3 decoding to ensure maximum recall,
	•	Designing a scalable memory-efficient pipeline.

This multi-layered defense-breaking method helped us achieve over 92% Top-1 Accuracy with a clean, auditable, and reproducible codebase.

---

## 🏁 **Conclusion**

Data protection is only as strong as its weakest anonymization layer.
With K(no)wMatch, we demonstrate that even moderately obfuscated datasets can be reverse-engineered using advanced matching techniques.

---

## 📺 Technical Walkthrough Video

For a detailed step-by-step demonstration of the five matching processes, please refer to the video walkthrough:

🔗 [Watch the Full Video Here](https://youtu.be/flNfQI4M_MA)

---

## ✍️**Team JAWAAN**

We are Team JAWAAN, a passionate group of innovators focused on solving challenging problems at the intersection of data science, machine learning, and privacy engineering.
	•	Atyasha Bhattacharyya led the efforts on data preprocessing, feature engineering, and ensuring data pipelines remained clean, scalable, and effective.
 
	•	Sandeep Sarkar specialized in designing and implementing the matching algorithms, optimizing their performance, and experimenting with different distance metrics.
 
	•	Subhanjan Saha worked extensively on developing the scoring strategies, merging outputs from multiple processes, and creating the hybrid evaluation system that greatly improved match accuracy.
 
	•	Ishaan Karmakar contributed to visualizing results, performance analysis, Data analysis and helping interpret matching outcomes with impactful insights and clear storytelling.

Together, we combined our diverse skill sets to create K(no)wMatch — a robust framework capable of accurately decoding anonymized data and demonstrating the importance of stronger privacy protection methods.


© 2025 | Team JAWAAN | K(no)wMatch
Built with ❤️, Python, and lots of Caffeine.
