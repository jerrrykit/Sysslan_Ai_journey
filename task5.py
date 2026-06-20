import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

def main():
    # Define paths
    data_file = 'Dataset1_processed.csv'
    output_dir = 'output_visuals'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load processed data
    df = pd.read_csv(data_file)
    
    # Define target
    y = df['Journey_Duration_Minutes']

    # ==========================================
    # Task 5.1: Train basic model (1 feature)
    # ==========================================
    basic_feature = ['Total_Distance']
    X_basic = df[basic_feature]
    
    # Split
    X_train_b, X_test_b, y_train, y_test = train_test_split(X_basic, y, test_size=0.2, random_state=42)
    
    # Train basic model (Linear Regression)
    basic_model = LinearRegression()
    basic_model.fit(X_train_b, y_train)
    
    # Evaluate
    y_pred_b = basic_model.predict(X_test_b)
    mae_b = mean_absolute_error(y_test, y_pred_b)
    rmse_b = np.sqrt(mean_squared_error(y_test, y_pred_b))

    # ==========================================
    # Task 5.2: Train improved model (multiple features)
    # ==========================================
    improved_features = ['Total_Distance', 'Number_of_Stops', 'Start_Departure_Minute', 'End_Arrival_Minute']
    X_improved = df[improved_features]
    
    # Split
    X_train_i, X_test_i, _, _ = train_test_split(X_improved, y, test_size=0.2, random_state=42)
    
    # Train improved model (Random Forest Regressor)
    improved_model = RandomForestRegressor(n_estimators=100, random_state=42)
    improved_model.fit(X_train_i, y_train)
    
    # Evaluate
    y_pred_i = improved_model.predict(X_test_i)
    mae_i = mean_absolute_error(y_test, y_pred_i)
    rmse_i = np.sqrt(mean_squared_error(y_test, y_pred_i))

    # ==========================================
    # Task 5.3 & 5.4: Compare models & Output
    # ==========================================
    with open('task5_output.txt', 'w') as f:
        f.write("Task 5: Model Comparison and Selection\n\n")
        f.write("--- Basic Model ---\n")
        f.write("Algorithm: Linear Regression\n")
        f.write(f"Feature(s): {', '.join(basic_feature)}\n")
        f.write(f"MAE: {mae_b:.2f} minutes\n")
        f.write(f"RMSE: {rmse_b:.2f} minutes\n\n")
        
        f.write("--- Improved Model ---\n")
        f.write("Algorithm: Random Forest Regressor\n")
        f.write(f"Feature(s): {', '.join(improved_features)}\n")
        f.write(f"MAE: {mae_i:.2f} minutes\n")
        f.write(f"RMSE: {rmse_i:.2f} minutes\n\n")
        
        f.write("--- Conclusion ---\n")
        if mae_i < mae_b and rmse_i < rmse_b:
            f.write("The Improved Model (Random Forest with multiple features) performs significantly better and is selected.\n")
        else:
            f.write("Review the metrics to select the better model.\n")

    # Visualization 1: Metrics Bar Chart
    labels = ['MAE', 'RMSE']
    basic_metrics = [mae_b, rmse_b]
    improved_metrics = [mae_i, rmse_i]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 6))
    rects1 = ax.bar(x - width/2, basic_metrics, width, label='Basic Model (LinReg, 1 Feature)', color='#87CEEB')
    rects2 = ax.bar(x + width/2, improved_metrics, width, label='Improved Model (RF, Multi-Feature)', color='#FA8072')

    ax.set_ylabel('Error (Minutes)', fontsize=12)
    ax.set_title('Task 5.3: Model Error Comparison', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.legend()

    # Add text labels on bars
    for rect in rects1 + rects2:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'model_comparison_metrics.png'))
    plt.close()
    
    # Visualization 2: Actual vs Predicted comparison subplot
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)
    
    # Define common min and max for consistent axes
    min_val = min(y_test.min(), y_pred_b.min(), y_pred_i.min())
    max_val = max(y_test.max(), y_pred_b.max(), y_pred_i.max())
    
    # Basic Model Plot
    axes[0].scatter(y_test, y_pred_b, alpha=0.5, color='#87CEEB')
    axes[0].plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    axes[0].set_title('Basic Model (Linear Regression)', fontsize=14)
    axes[0].set_xlabel('Actual Duration (minutes)', fontsize=12)
    axes[0].set_ylabel('Predicted Duration (minutes)', fontsize=12)
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.6)
    
    # Improved Model Plot
    axes[1].scatter(y_test, y_pred_i, alpha=0.5, color='#FA8072')
    axes[1].plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    axes[1].set_title('Improved Model (Random Forest)', fontsize=14)
    axes[1].set_xlabel('Actual Duration (minutes)', fontsize=12)
    axes[1].legend()
    axes[1].grid(True, linestyle='--', alpha=0.6)
    
    plt.suptitle('Task 5.4: Actual vs Predicted Values Comparison', fontsize=16)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'model_comparison_scatter.png'))
    plt.close()
    
    print("Task 5 execution completed successfully.")

if __name__ == "__main__":
    main()
