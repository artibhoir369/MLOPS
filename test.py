import requests
import numpy as np

# Test data with features and the actual labels
test_data = [
    {"features": [5.1, 3.5, 1.4, 0.2], "actual_label": 0},
    {"features": [4.9, 3.0, 1.4, 0.2], "actual_label": 0},
    {"features": [6.7, 1.3, 4.7, 1.5], "actual_label": 1},
    {"features": [5.9, 3.0, 5.1, 1.8], "actual_label": 2},
    {"features": [5.1, 3.6, 1.5, 0.2], "actual_label": 1},
    {"features": [7.0, 2.0, 5.5, 2.0], "actual_label": 0},
]

# Send the requests to the model API and compare predictions
correct_predictions = 0
for data in test_data:
    response = requests.post("http://localhost:8080/predict", json={"features": data["features"]})
    prediction = response.json()["prediction"]
    actual_label = data["actual_label"]
    
    if prediction == actual_label:
        correct_predictions += 1

# Calculate accuracy
accuracy = correct_predictions / len(test_data)
print(f"Accuracy: {accuracy * 100:.2f}%")
