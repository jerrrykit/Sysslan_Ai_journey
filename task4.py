import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def main():
    # Define paths
    data_file = 'Dataset1_processed.csv'
    output_dir = 'output_visuals'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load processed data
    df = pd.read_csv(data_file)

    # Task 4.1: Split the dataset into training and testing sets
    features = ['Total_Distance', 'Number_of_Stops', 'Start_Departure_Minute', 'End_Arrival_Minute']
    X = df[features]
    y = df['Journey_Duration_Minutes']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Task 4.2: Train a Linear Regression model using training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Task 4.3: Evaluate model accuracy using MAE and RMSE
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    with open('task4_output.txt', 'w') as f:
        f.write("Task 4: Model Training and Evaluation\n")
        f.write(f"Model used: Linear Regression\n")
        f.write(f"Features used: {', '.join(features)}\n")
        f.write(f"Mean Absolute Error (MAE): {mae:.2f} minutes\n")
        f.write(f"Root Mean Squared Error (RMSE): {rmse:.2f} minutes\n")

    # Task 4.4: Visualize actual vs predicted journey durations
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='teal')
    
    # Plot perfect prediction line
    max_val = max(y_test.max(), y_pred.max())
    min_val = min(y_test.min(), y_pred.min())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction')

    plt.title('Task 4.4: Actual vs Predicted Journey Durations', fontsize=14)
    plt.xlabel('Actual Journey Duration (minutes)', fontsize=12)
    plt.ylabel('Predicted Journey Duration (minutes)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig(os.path.join(output_dir, 'actual_vs_predicted.png'))
    plt.close()

if __name__ == "__main__":
    main()
