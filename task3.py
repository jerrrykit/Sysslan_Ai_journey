import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Define paths
    data_file = 'Dataset1_processed.csv'
    output_dir = 'output_visuals'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load processed data
    df = pd.read_csv(data_file)

    # Task 3.1: Visualize how distance affects journey duration
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Total_Distance'], df['Journey_Duration_Minutes'], alpha=0.5, color='steelblue')
    plt.title('Task 3.1: Impact of Total Distance on Journey Duration', fontsize=14)
    plt.xlabel('Total Distance (km)', fontsize=12)
    plt.ylabel('Journey Duration (minutes)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'distance_vs_duration.png'))
    plt.close()

    # Task 3.2: Visualize the impact of number of stops on journey duration
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Number_of_Stops'], df['Journey_Duration_Minutes'], alpha=0.5, color='darkorange')
    plt.title('Task 3.2: Impact of Number of Stops on Journey Duration', fontsize=14)
    plt.xlabel('Number of Stops', fontsize=12)
    plt.ylabel('Journey Duration (minutes)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'stops_vs_duration.png'))
    plt.close()

    # Task 3.3: Correlation visuals between input features and journey duration
    # Since seaborn isn't available, we will use matplotlib's matshow or just print the table and do a simple plot
    plt.figure(figsize=(8, 8))
    features = ['Total_Distance', 'Number_of_Stops', 'Start_Departure_Minute', 'End_Arrival_Minute', 'Journey_Duration_Minutes']
    correlation_matrix = df[features].corr()
    cax = plt.matshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
    plt.colorbar(cax)
    plt.xticks(range(len(features)), features, rotation=45, ha='left')
    plt.yticks(range(len(features)), features)
    for i in range(len(features)):
        for j in range(len(features)):
            plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black')
    plt.title('Task 3.3: Correlation Heatmap', pad=20)
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'), bbox_inches='tight')
    plt.close()

    # Task 3.4: Build a pivot table summarizing number of stops for each train
    pivot_table = pd.pivot_table(df, values='Number_of_Stops', index='Train_No')
    top_stops = pivot_table.sort_values(by='Number_of_Stops', ascending=False).head(10)
    
    df['Distance_Bin'] = pd.cut(df['Total_Distance'], bins=[0, 500, 1000, 2000, 5000], labels=['0-500km', '500-1000km', '1000-2000km', '2000km+'])
    stops_summary_pivot = pd.pivot_table(df, values='Number_of_Stops', index='Distance_Bin', aggfunc=['mean', 'max', 'min', 'count'])
    
    with open('task3_output.txt', 'w') as f:
        f.write("Task 3.4: Pivot table summarizing number of stops for each train (Top 10)\n")
        f.write(top_stops.to_string() + "\n\n")
        f.write("Pivot Table: Summary of Stops by Distance Bins\n")
        f.write(stops_summary_pivot.to_string() + "\n")

if __name__ == "__main__":
    main()
