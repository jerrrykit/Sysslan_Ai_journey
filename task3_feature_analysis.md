# Task 3: Feature Analysis with Visuals

## Task 3.1: Distance vs. Journey Duration
A scatter plot was created to visualize how the total distance of a train journey affects its duration. As expected, there is a strong positive correlation—longer distances generally result in longer journey durations. 

![Distance vs Duration](output_visuals/distance_vs_duration.png)

## Task 3.2: Number of Stops vs. Journey Duration
This scatter plot visualizes the impact of the number of stops on the journey duration. Similar to distance, more stops generally lead to a longer journey time, but the spread increases for trains with many stops (likely due to varying wait times and distances between stops).

![Stops vs Duration](output_visuals/stops_vs_duration.png)

## Task 3.3: Correlation Analysis
A correlation heatmap was generated to quantify the linear relationships between the input features and the target variable (`Journey_Duration_Minutes`).

![Correlation Heatmap](output_visuals/correlation_heatmap.png)

**Key Insights:**
- `Total_Distance` has the highest correlation with `Journey_Duration_Minutes`.
- `Number_of_Stops` is also highly correlated with the duration.
- The start and end times (in minutes from midnight) show very low correlation, indicating that the time of day a train departs doesn't heavily predict the total length of the journey on its own.

## Task 3.4: Pivot Table Summaries
To summarize the number of stops across different trains, two pivot tables were created.

**Top 10 Trains with the Most Stops:**
| Train_No | Number_of_Stops |
|----------|-----------------|
| 53041    | 118 |
| 13007    | 112 |
| 13049    | 111 |
| 58112    | 109 |
| 13008    | 108 |
| 53042    | 107 |
| 13050    | 106 |
| 58111    | 102 |
| 19019    | 98 |
| 13352    | 97 |

**Summary of Stops by Distance Bins:**
Grouping the trains by distance brackets reveals how the number of stops scales with the journey length.

| Distance Bin | Average Stops | Max Stops | Min Stops | Number of Trains |
|--------------|---------------|-----------|-----------|------------------|
| **0-500 km** | 14.2 | 83 | 2 | 8,909 |
| **500-1000 km** | 23.7 | 118 | 2 | 902 |
| **1000-2000 km**| 26.9 | 112 | 2 | 916 |
| **2000+ km** | 34.5 | 97 | 6 | 386 |

