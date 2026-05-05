# Customer Churn Prediction Project

This project aims to predict which customers are likely to leave a service provider (churn) based on their usage patterns and demographics. By identifying these customers early, businesses can take proactive steps to retain them.
📊 Project Workflow
This graph illustrates the end-to-end pipeline from data ingestion to model output:
1- Data Loading: Importing the raw customer dataset. 
2- Wrangling: Cleaning data types, handling missing values in TotalCharges, and mapping binary features. 
3- Preprocessing: Using OrdinalEncoder to convert categorical text into numbers that the model can understand. 
4- Resampling: Implementing RandomOverSampler or RandomUnderSampler to fix the class imbalance between "Churn" and "No Churn".
5- Modeling: Training a DecisionTreeClassifier within a Scikit-Learn pipeline.  
6- Prediction: Generating results on new data to identify at-risk customers. 

🛠️ Tech StackLanguage: 
Python Libraries: Pandas, Scikit-Learn, Imbalanced-Learn.  
Tools: Jupyter Notebooks for experimentation.

📁 Project Structure
notebook.ipynb: The main experimentation file containing data analysis and model training. 
helper_functions.py: Contains custom functions for data cleaning (wrangle) and generating new predictions. 
model-1: The serialized (saved) version of the trained model for future use.  
