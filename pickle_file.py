can use model using :

# Save scaler and encoders

import pickle

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("label_encoder_gender.pkl", "wb") as f:
    pickle.dump(LB, f)

with open("onehot_encoder_geo.pkl", "wb") as f:
    pickle.dump(onehot_encoder_geo, f)

print("Model, scaler and encoders saved successfully.")



import tensorflow as tf
import pickle
import numpy as np
import pandas as pd

# Load Model
model = tf.keras.models.load_model("model.keras")

# Load Scaler and Encoders
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("label_encoder_gender.pkl", "rb") as f:
    LB = pickle.load(f)

with open("onehot_encoder_geo.pkl", "rb") as f:
    onehot_encoder_geo = pickle.load(f)

# ------------------ USER INPUT ------------------

CreditScore = float(input("Enter Credit Score: "))
Geography = input("Enter Geography (France/Germany/Spain): ").strip().capitalize()
Gender = input("Enter Gender (Male/Female): ").strip().capitalize()
Age = int(input("Enter Age: "))
Tenure = int(input("Enter Tenure: "))
Balance = float(input("Enter Balance: "))
NumOfProducts = int(input("Enter Number of Products: "))
HasCrCard = int(input("Has Credit Card (1=Yes, 0=No): "))
IsActiveMember = int(input("Is Active Member (1=Yes, 0=No): "))
EstimatedSalary = float(input("Enter Estimated Salary: "))

# Encode Gender
gender_encoded = LB.transform([Gender])[0]

# Encode Geography
geo_encoded = onehot_encoder_geo.transform(
    pd.DataFrame([[Geography]], columns=["Geography"])
).toarray()

# Create Input
new_data = np.array([[
    CreditScore,
    gender_encoded,
    Age,
    Tenure,
    Balance,
    NumOfProducts,
    HasCrCard,
    IsActiveMember,
    EstimatedSalary
]])

# Combine Geography Encoding
new_data = np.concatenate((new_data, geo_encoded), axis=1)

# Scale Input
new_data = scaler.transform(new_data)

# Prediction
prediction = model.predict(new_data, verbose=0)

print("\nPrediction Probability:", prediction[0][0])

if prediction[0][0] >= 0.5:
    print("Customer is likely to LEAVE the bank.")
else:
    print("Customer is likely to STAY with the bank.")
