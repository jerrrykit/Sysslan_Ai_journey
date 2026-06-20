from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import os

app = Flask(__name__)

# Initialize model variable
model = None
features = ['Total_Distance', 'Number_of_Stops', 'Start_Departure_Minute', 'End_Arrival_Minute']

def load_and_train_model():
    global model
    print("Loading data and training model...")
    data_file = 'Dataset1_processed.csv'
    
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"Data file {data_file} not found.")
        
    df = pd.read_csv(data_file)
    X = df[features]
    y = df['Journey_Duration_Minutes']
    
    # Train model (using same parameters as task 5 & 6)
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training complete.")

# Train the model when the app starts
load_and_train_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features from request
        dist = float(data.get('distance'))
        stops = float(data.get('stops'))
        start_min = float(data.get('start_time'))
        end_min = float(data.get('end_time'))
        
        # Create input dataframe
        user_input = pd.DataFrame([[dist, stops, start_min, end_min]], columns=features)
        
        # Predict
        prediction = model.predict(user_input)[0]
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    # Run the app on localhost
    app.run(host='0.0.0.0', port=5000, debug=True)
