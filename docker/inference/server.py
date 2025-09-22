from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# TODO: Load the trained model from the shared volume (use the correct path)
model = ...

# TODO: Add request method to predict
@app.route('/predict', methods=[''])
def predict():
    # TODO: Get the input array from the request body and make prediction using the model
    get_json = request.get_json()
    iris_input = ...

    # HINT: use np.array().reshape(1, -1) to convert input to 2D array
    prediction = ...

    return ...

@app.route('/')
def hello():
    return 'Welcome to Docker Lab'

if __name__ == '__main__':
    #Run the Flask app (bind it to port 8080 or any other port)
    app.run(debug=True, port=8080, host='0.0.0.0')
