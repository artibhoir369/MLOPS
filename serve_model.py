from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary
import time
import joblib
import numpy as np

# Start the Prometheus metrics server
start_http_server(8000)  # Prometheus will scrape metrics from this port

# Define a metric to measure request latency
REQUEST_LATENCY = Summary('request_latency_seconds', 'Latency of prediction requests')

# Load the trained model
model = joblib.load('model.joblib')

# Initialize Flask app
app = Flask(__name__)

@REQUEST_LATENCY.time()
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON request data
    data = request.get_json()

    # Convert to numpy array (assuming input is a list of features)
    features = np.array(data['features']).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Return prediction as JSON response
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
