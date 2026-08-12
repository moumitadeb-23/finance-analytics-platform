import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("=" * 60)
print("Finance AI Assistant")
print("Random Forest Fraud Detection")
print("=" * 60)

# ====================================
# Load Dataset
# ====================================

DATASET = "dataset/credit_card_transactions.csv"

df = pd.read_csv(DATASET)

print("\nDataset Loaded Successfully")
print(df.shape)

# ====================================
# Remove Missing Values
# ====================================

df = df.dropna().copy()

# ====================================
# (Optional) Use a smaller sample for faster training
# Comment this block if you want to train on the full dataset
# ====================================

df = df.sample(
    n=200000,
    random_state=42
)

print("\nTraining Dataset Size")
print(df.shape)

# ====================================
# Features
# ====================================

features = [
    "merchant",
    "category",
    "amt",
    "gender",
    "city",
    "state",
    "job"
]

target = "is_fraud"

# ====================================
# Encode Text Columns
# ====================================

encoders = {}

for col in features:

    if not pd.api.types.is_numeric_dtype(df[col]):

        le = LabelEncoder()

        df[col] = le.fit_transform(
            df[col].astype(str)
        )

        encoders[col] = le

print("\nEncoding Completed")

print(df[features].dtypes)

# ====================================
# Feature Matrix
# ====================================

X = df[features]

y = df[target]

# ====================================
# Train/Test Split
# ====================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ====================================
# Random Forest Model
# ====================================

print("\nTraining Model...")

model = RandomForestClassifier(

    n_estimators=100,

    random_state=42,

    n_jobs=-1

)

model.fit(

    X_train,

    y_train

)

print("Training Complete")

# ====================================
# Prediction
# ====================================

predictions = model.predict(X_test)

# ====================================
# Accuracy
# ====================================

accuracy = accuracy_score(

    y_test,

    predictions

)

print("\nAccuracy : {:.2f}%".format(accuracy * 100))

# ====================================
# Confusion Matrix
# ====================================

print("\nConfusion Matrix")

print(

    confusion_matrix(

        y_test,

        predictions

    )

)

# ====================================
# Classification Report
# ====================================

print("\nClassification Report")

print(

    classification_report(

        y_test,

        predictions

    )

)

# ====================================
# Save Model
# ====================================

os.makedirs("models", exist_ok=True)

joblib.dump(

    model,

    "models/fraud_model.pkl"

)

joblib.dump(

    encoders,

    "models/encoders.pkl"

)

print("\nModel Saved Successfully")

print("models/fraud_model.pkl")

print("models/encoders.pkl")