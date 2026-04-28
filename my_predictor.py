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
    return df