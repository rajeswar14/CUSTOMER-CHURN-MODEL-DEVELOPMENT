# Customer Churn Analysis

This repository contains a Jupyter Notebook for a customer churn analysis project. The goal of this analysis is to understand the factors contributing to customer churn and to build a model to predict churn probability. This can help businesses retain customers by identifying at-risk individuals and proactively engaging with them.

## Project Overview

Customer churn analysis is crucial for businesses as retaining customers is often more cost-effective than acquiring new ones. By analyzing patterns in customer behavior, we can better understand which factors lead to churn and develop strategies to reduce it. This project includes data exploration, feature engineering, and modeling to predict customer churn.

## Notebook Contents

The Jupyter Notebook, `customer churn project.ipynb`, includes the following sections:

1. **Data Loading and Exploration**:  
   - Load the dataset and check for missing values, data types, and basic statistics.
2. **Data Preprocessing**:  
   - Handle missing values and data encoding (if necessary).
   - Scale/normalize features to prepare the data for modeling.

3. **Feature Engineering**:  
   - Engineer new features that could improve the predictive performance of the model.
   - Select relevant features for the model.

4. **Modeling**:  
   - Train various machine learning models (e.g., Logistic Regression, Decision Trees, Random Forest,Gradient Boosting,KNN etc.) to predict churn.
   - Evaluate models using appropriate metrics (e.g., accuracy, precision, recall, F1-score, AUC-ROC).

5. **Model Evaluation and Selection**:  
   - Compare model performance to select the best model for predicting customer churn.
   - Analyze feature importance to gain insights into key churn drivers.

6. **Deployment with Streamlit:**  
   - Developed an interactive **web app** for real-time predictions.  
   - Users can input customer details and get instant **churn predictions**.  

7. **Conclusion and Insights**:  
   - Summarize findings from the analysis and offer recommendations for churn mitigation.

## Requirements

To run the notebook, you need the following libraries installed:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`

You can install these packages via pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
