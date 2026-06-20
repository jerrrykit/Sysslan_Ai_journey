import pandas as pd
import numpy as np

def time_to_minutes(t_str):
    if pd.isna(t_str): return 0
    parts = str(t_str).split(':')
    if len(parts) >= 2:
        return int(parts[0]) * 60 + int(parts[1]) + (int(parts[2])/60.0 if len(parts) > 2 else 0)
    return 0

def process_data():
    df = pd.read_csv('Dataset1.csv')
    
    # Task 2.1: Handle missing values and remove duplicate records
    initial_shape = df.shape
    df = df.drop_duplicates()
    df = df.dropna()
    post_cleaning_shape = df.shape

    # Sort by Train_No and SN just to be sure
    df = df.sort_values(by=['Train_No', 'SN'])

    # Convert time to minutes for calculations
    df['Arr_Min'] = df['Arrival_time'].apply(time_to_minutes)
    df['Dep_Min'] = df['Departure_Time'].apply(time_to_minutes)

    train_data = []
    
    # Group by train
    for train_no, group in df.groupby('Train_No'):
        # Task 2.4: Create input features
        total_distance = group['Distance'].max()
        num_stops = group['SN'].max()
        
        # Start and End times
        start_dep = group.iloc[0]['Dep_Min']
        end_arr = group.iloc[-1]['Arr_Min']
        
        # Task 2.3: Calculate total journey duration
        # We accumulate differences to handle midnight crossings accurately
        duration = 0
        current_time = start_dep
        
        for idx in range(1, len(group)):
            arr_time = group.iloc[idx]['Arr_Min']
            diff = arr_time - current_time
            if diff < 0:
                diff += 24 * 60
            duration += diff
            current_time = arr_time
            
            # Don't add wait time at the very last station
            if idx < len(group) - 1:
                dep_time = group.iloc[idx]['Dep_Min']
                diff = dep_time - current_time
                if diff < 0:
                    diff += 24 * 60
                duration += diff
                current_time = dep_time
                
        train_data.append({
            'Train_No': train_no,
            'Total_Distance': total_distance,
            'Number_of_Stops': num_stops,
            'Start_Departure_Minute': start_dep,
            'End_Arrival_Minute': end_arr,
            'Journey_Duration_Minutes': duration
        })

    # Create final train-level dataframe
    df_trains = pd.DataFrame(train_data)
    
    # Save the processed dataset
    output_file = 'Dataset1_processed.csv'
    df_trains.to_csv(output_file, index=False)

    # Output summary
    with open('task2_output.txt', 'w') as f:
        f.write(f"Task 2.1: Missing values and duplicates\n")
        f.write(f"Original records: {initial_shape[0]}, Cleaned records: {post_cleaning_shape[0]}\n\n")
        
        f.write("Task 2.2: Arrival and departure times conversion\n")
        f.write("Times were converted to minutes from midnight (e.g., 10:25:00 -> 625 minutes) to facilitate calculations and serve as numerical features.\n\n")
        
        f.write("Task 2.3 & 2.4: Journey Duration & Input Features\n")
        f.write(f"Processed features for {len(df_trains)} trains.\n")
        f.write("Sample processed data (first 5 rows):\n")
        f.write(df_trains.head().to_string() + "\n\n")
        
        f.write("Summary Statistics of Processed Data:\n")
        f.write(df_trains.describe().to_string() + "\n")
        
if __name__ == "__main__":
    process_data()
