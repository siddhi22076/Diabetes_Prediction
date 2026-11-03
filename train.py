import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("diabetes.csv")

# Features and Target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("="*40)
print("Diabetes Prediction Model")
print("="*40)

print(f"Accuracy : {accuracy*100:.2f}%")

st.sidebar.title("Model Information")
st.sidebar.success("Algorithm: Random Forest")
st.sidebar.info("Accuracy: 76%")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "diabetes_model.pkl")

print("\nModel Saved Successfully!")