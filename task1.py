import pandas as pd

def main():
    # Load dataset
    df = pd.read_csv('Dataset1.csv')
    
    with open('task1_output.txt', 'w') as f:
        f.write("--- Task 1.1: Total records and columns ---\n")
        f.write(f"Total records: {df.shape[0]}\n")
        f.write(f"Total columns: {df.shape[1]}\n")
        f.write(f"Columns: {df.columns.tolist()}\n")
        
        f.write("\n--- Task 1.2: Train-wise table showing starting and ending stations ---\n")
        df = df.sort_values(by=['Train_No', 'SN'])
        train_wise_stations = df.groupby('Train_No').agg(
            Starting_Station=('Station_Name', 'first'),
            Ending_Station=('Station_Name', 'last')
        ).reset_index()
        f.write(train_wise_stations.head(10).to_string() + "\n")
        
        f.write("\n--- Task 1.3: Basic statistics for distance and number of stops ---\n")
        train_stats = df.groupby('Train_No').agg(
            Total_Distance=('Distance', 'max'),
            Number_of_Stops=('SN', 'max')
        )
        f.write("Statistics for Distance:\n")
        f.write(train_stats['Total_Distance'].describe().to_string() + "\n")
        f.write("\nStatistics for Number of Stops:\n")
        f.write(train_stats['Number_of_Stops'].describe().to_string() + "\n")
        
        f.write("\n--- Task 1.4: Missing, duplicate, or incorrect values ---\n")
        f.write("Missing values per column:\n")
        f.write(df.isnull().sum().to_string() + "\n")
        f.write(f"\nDuplicate rows: {df.duplicated().sum()}\n")
        negative_distances = (df['Distance'] < 0).sum()
        f.write(f"Rows with negative distance: {negative_distances}\n")
        zero_sn = (df['SN'] <= 0).sum()
        f.write(f"Rows with SN <= 0: {zero_sn}\n")

if __name__ == "__main__":
    main()
