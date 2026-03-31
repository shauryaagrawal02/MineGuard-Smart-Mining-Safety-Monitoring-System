import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

print("MineGuard AI Safety System\n")

def rule_based(gas, temp, humidity, depth):
    if gas > 500 or temp > 80 or humidity > 100 or depth > 800:
        return "HIGH"

    risk_score = 0

    if gas > 300:
        risk_score += 3
    elif gas > 150:
        risk_score += 2

    if temp > 40:
        risk_score += 2
    elif temp < 10:
        risk_score += 1

    if humidity > 85:
        risk_score += 1

    if depth > 500:
        risk_score += 2

    if risk_score >= 6:
        return "HIGH"
    elif risk_score >= 3:
        return "MEDIUM"
    else:
        return "LOW"

data = []

for _ in range(300):
    gas = np.random.randint(50, 600)
    temp = np.random.randint(5, 100)
    humidity = np.random.randint(10, 100)
    depth = np.random.randint(50, 900)

    risk = rule_based(gas, temp, humidity, depth)
    data.append([gas, temp, humidity, depth, risk])

df = pd.DataFrame(data, columns=["Gas", "Temp", "Humidity", "Depth", "Risk"])

X = df[["Gas", "Temp", "Humidity", "Depth"]]
y = df["Risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("\nFeature Importance:")
for f, i in zip(X.columns, model.feature_importances_):
    print(f, ":", round(i * 100, 2), "%")

print("\nEnter Mine Conditions:")
gas = float(input("Gas (ppm): "))
temp = float(input("Temperature (°C): "))
humidity = float(input("Humidity (%): "))
depth = float(input("Depth (m): "))

input_data = pd.DataFrame([[gas, temp, humidity, depth]], columns=["Gas", "Temp", "Humidity", "Depth"])

ml_prediction = model.predict(input_data)[0]
rule_prediction = rule_based(gas, temp, humidity, depth)

print("\nRESULTS")
print("ML Prediction:", ml_prediction)
print("Rule-Based Prediction:", rule_prediction)

if ml_prediction == rule_prediction:
    print("Both systems agree")
else:
    print("Difference detected")

print("\nThank you for using MineGuard")
