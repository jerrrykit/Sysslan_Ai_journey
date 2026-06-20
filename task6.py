import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import warnings

# Suppress warnings for cleaner interactive console
warnings.filterwarnings('ignore')

def main():
    print("="*60)
    print("🚆 Train Journey Duration Predictor (Level 6) 🚆")
    print("="*60)
    print("Initializing system and training the model...")

    # Define paths
    data_file = 'Dataset1_processed.csv'
    output_dir = 'output_visuals'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load data
    try:
        df = pd.read_csv(data_file)
    except FileNotFoundError:
        print(f"Error: {data_file} not found. Please ensure data is processed.")
        return

    features = ['Total_Distance', 'Number_of_Stops', 'Start_Departure_Minute', 'End_Arrival_Minute']
    X = df[features]
    y = df['Journey_Duration_Minutes']

    # Train model using the best algorithm from Task 5
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Generate baseline visualization
    print("Generating baseline visualization on historical test data...")
    y_pred = model.predict(X_test)
    
    # Initialize the interactive plot figure
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.2, color='gray', label='Historical Data Predictions')
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    plt.title('Predicted vs Actual Journey Durations')
    plt.xlabel('Actual Duration (minutes)')
    plt.ylabel('Predicted Duration (minutes)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    base_fig_path = os.path.join(output_dir, 'interactive_base.png')
    plt.savefig(base_fig_path)
    print(f"Baseline visualization saved to: {base_fig_path}")
    print("\n✅ System Ready!\n")

    def get_float_input(prompt):
        while True:
            try:
                val = input(prompt).strip()
                if not val:
                    print("❌ Input cannot be empty. Please type a number and press Enter.")
                    continue
                return float(val)
            except ValueError:
                print("❌ Invalid input! Please enter numerical values only.")
            except EOFError:
                print("\nInput stream closed. Exiting.")
                exit(0)

    user_interactions = 0

    while True:
        try:
            print("-" * 40)
            print("📝 Enter Journey Details:")
            dist = get_float_input("Total Distance (e.g., 500): ")
            stops = get_float_input("Number of Stops (e.g., 5): ")
            start_min = get_float_input("Start Departure Minute of Day (e.g., 600 for 10:00 AM): ")
            end_min = get_float_input("End Arrival Minute of Day (e.g., 900 for 3:00 PM): ")
            
            # Predict
            user_input = pd.DataFrame([[dist, stops, start_min, end_min]], columns=features)
            predicted_duration = model.predict(user_input)[0]
            
            print(f"\n✨ => PREDICTED JOURNEY DURATION: {predicted_duration:.2f} minutes")
            
            # Interactive Plotting
            knows_actual = input("\nDo you know the ACTUAL duration for this journey? (y/n): ").strip().lower()
            if knows_actual == 'y':
                actual_duration = get_float_input("Enter actual duration in minutes: ")
                user_interactions += 1
                
                # Add this point to the plot
                plt.scatter([actual_duration], [predicted_duration], 
                            color='red', s=100, edgecolor='black', zorder=5, 
                            label='Your User Input' if user_interactions == 1 else "")
                
                # Update legend to avoid duplicates
                handles, labels = plt.gca().get_legend_handles_labels()
                by_label = dict(zip(labels, handles))
                plt.legend(by_label.values(), by_label.keys())
                
                user_fig_path = os.path.join(output_dir, 'interactive_user_prediction.png')
                plt.savefig(user_fig_path)
                print(f"📈 Visualization updated with your journey! Saved to: {user_fig_path}")
                error = abs(actual_duration - predicted_duration)
                print(f"   Prediction Error: {error:.2f} minutes")
            
            cont = input("\nDo you want to make another prediction? (y/n): ").strip().lower()
            if cont != 'y':
                print("\nExiting Interactive Predictor. Goodbye! 👋")
                plt.close()
                break
                
        except KeyboardInterrupt:
            print("\nExiting Interactive Predictor. Goodbye! 👋")
            plt.close()
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
