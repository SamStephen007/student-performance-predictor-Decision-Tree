# student_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv("Student_Performance.csv")

# Encode categorical
le = LabelEncoder()
df['Extracurricular Activities'] = le.fit_transform(df['Extracurricular Activities'])

# Convert Performance Index to class
def classify(score):
    if score < 50:
        return 0  # Low
    elif score < 75:
        return 1  # Medium
    else:
        return 2  # High

df['Performance Class'] = df['Performance Index'].apply(classify)

# Features and labels
X = df.drop(['Performance Index', 'Performance Class'], axis=1)
y = df['Performance Class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree model
model = DecisionTreeClassifier(criterion="entropy", max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model using pickle
with open('student_performance_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Decision Tree model trained and saved successfully.")
