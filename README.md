# Customer Churn Prediction Project <br>

This project aims to predict which customers are likely to leave a service provider (churn) based on their usage patterns and demographics. By identifying these customers early, businesses can take proactive steps to retain them. <br> <br>

📊 Project Workflow <br>
This graph illustrates the end-to-end pipeline from data ingestion to model output: <br>
1- Data Loading: Importing the raw customer dataset.  <br>
2- Wrangling: Cleaning data types, handling missing values in TotalCharges, and mapping binary features.  <br>
3- Preprocessing: Using OrdinalEncoder to convert categorical text into numbers that the model can understand.  <br>
4- Resampling: Implementing RandomOverSampler or RandomUnderSampler to fix the class imbalance between "Churn" and "No Churn". <br>
5- Modeling: Training a DecisionTreeClassifier within a Scikit-Learn pipeline.   <br>
6- Prediction: Generating results on new data to identify at-risk customers.  <br> <br>

🛠️ Tech StackLanguage:  <br>
Python Libraries: Pandas, Scikit-Learn, Imbalanced-Learn.   <br>
Tools: Jupyter Notebooks for experimentation. <br> <br>

📁 Project Structure <br>
notebook.ipynb: The main experimentation file containing data analysis and model training.  <br>
helper_functions.py: Contains custom functions for data cleaning (wrangle) and generating new predictions.  <br>
model-1: The serialized (saved) version of the trained model for future use.  
