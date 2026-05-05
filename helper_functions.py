import pickle
import pandas as pd

def wrangle(file):
    df = pd.read_csv(file).set_index("customerID")

    #convert cat featurs to numeric
    mapping = {"No":0, "Yes":1}
    df["Partner"] = df["Partner"].map(mapping)
    df["Dependents"] = df["Dependents"].map(mapping)
    df["PhoneService"] = df["PhoneService"].map(mapping)
    df["PaperlessBilling"] = df["PaperlessBilling"].map(mapping)
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["Churn"] = df["Churn"].map(mapping)
    df.dropna(inplace=True)
    return df

def make_predictions(data_filepath, model_filepath):
    # Wrangle JSON file
    X_test = wrangle(data_filepath)
    # Load model
    with open(model_filepath,"rb") as f:
        model = pickle.load(f)
        
    # Generate predictions
    y_test_pred = model.predict(X_test)
    # Put predictions into Series with name "bankrupt", and same index as X_test
    y_test_pred = pd.Series(y_test_pred, index=X_test.index, name="bankrupt")
    return y_test_pred
