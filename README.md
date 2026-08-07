# customer-churn-prediction-using-deep-learning


A Deep Learning project that predicts whether a bank customer is likely to leave the bank (churn) or stay using an Artificial Neural Network (ANN) built with TensorFlow and Keras.

---

## Project Overview

Customer churn prediction is an important business problem in the banking industry. This project uses customer information such as credit score, geography, age, balance, and salary to predict whether a customer will leave the bank.

The model is trained using an Artificial Neural Network (ANN) and achieves approximately **80% validation accuracy**.

---

## Dataset

**Dataset:** Churn_Modelling.csv

The dataset contains information about bank customers, including:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary
- Exited (Target Variable)

### Target Variable

- **0** → Customer Stays
- **1** → Customer Leaves

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- TensorFlow
- Keras
- Matplotlib
- Jupyter Notebook

---

## Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Preprocessing
4. Label Encoding
5. One-Hot Encoding
6. Feature Scaling
7. Train-Test Split
8. Build ANN Model
9. Train Model
10. Evaluate Performance
11. Save Model and Encoders
12. Predict Customer Churn

---

## ANN Architecture

```
Input Layer (12 Features)
        │
        ▼
Dense Layer (64 Neurons, ReLU)
        │
        ▼
Dense Layer (32 Neurons, ReLU)
        │
        ▼
Output Layer (1 Neuron, Sigmoid)
```

---

## Model Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Metric | Accuracy |
| Activation | ReLU, Sigmoid |

---

## Model Performance

Validation Accuracy:

```
Approximately 80%
```

---

## Project Structure

```
customer-churn-prediction-using-deep-learning/

│── ANN_churn_prediction_main.ipynb
│── prediction.ipynb
│── Churn_Modelling.csv
│── model.keras
│── scaler.pkl
│── label_encoder_gender.pkl
│── onehot_encoder_geo.pkl
│── requirements.txt
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/customer-churn-prediction-using-deep-learning.git
```

Move to the project folder

```bash
cd customer-churn-prediction-using-deep-learning
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

Open Jupyter Notebook

```bash
jupyter notebook
```

Run

```
ANN_churn_prediction_main.ipynb
```

or

```
prediction.ipynb
```

---

## Future Improvements

- Improve model accuracy
- Build a Streamlit web application
- Deploy the model using Render or Hugging Face Spaces
- Hyperparameter tuning
- Handle class imbalance

---

## Author

**Karthik Kumar**

GitHub:
https://github.com/KarthikKumar293

---

## License

This project is created for learning and educational purposes.
