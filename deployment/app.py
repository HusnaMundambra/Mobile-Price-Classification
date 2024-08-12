from flask import Flask, request, render_template
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_mobile_price():
    # Extract input features from the form
    battery_power = int(request.form.get('battery_power'))
    px_height = int(request.form.get('px_height'))
    px_width = int(request.form.get('px_width'))
    ram = int(request.form.get('ram'))
    primary_cam_MP = int(request.form.get('primary_cam_MP'))
    front_cam_MP = int(request.form.get('front_cam_MP'))
    screen_height = int(request.form.get('screen_height'))

    # Create a numpy array with the inputs
    features = np.array([battery_power, px_height, px_width, ram, primary_cam_MP, front_cam_MP, screen_height]).reshape(1, -1)

    # Predict the price using the model
    result = model.predict(features)

    # Return the result as a string
    return str(result[0])

if __name__ == "__main__":
    app.run(debug=True, port=8080)

