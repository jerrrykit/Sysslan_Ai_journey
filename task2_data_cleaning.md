# Task 2: Data Cleaning and Feature Creation

## Task 2.1: Handling Missing Values and Duplicates
- **Initial records:** 186,074
- **Cleaned records:** 186,074
- **Notes:** No missing values or duplicate records were found in the dataset, so no data was dropped.

## Task 2.2: Time Format Conversion
- Arrival and Departure times (e.g., `10:25:00`) were successfully converted to **minutes from midnight** (e.g., `625.0` minutes). This continuous numerical format is machine-learning friendly and makes duration arithmetic straightforward.

## Task 2.3 & 2.4: Journey Duration & Input Features
The dataset was transformed into a train-wise dataset with **11,113 unique trains**. Each row now represents a single train journey.

**New Input Features Created:**
- `Start_Departure_Minute`: Time the train left its origin (in minutes from midnight).
- `End_Arrival_Minute`: Time the train arrived at its final destination.
- `Total_Distance`: Total cumulative distance of the journey.
- `Number_of_Stops`: Total number of stations the train stopped at.

**Target Variable Created:**
- `Journey_Duration_Minutes`: Calculated overall duration from origin departure to final destination arrival, properly accounting for multi-day trips and midnight crossovers.

### Sample Processed Data (First 5 Trains)
| Train_No | Total_Distance | Number_of_Stops | Start_Departure_Minute | End_Arrival_Minute | Journey_Duration_Minutes |
|----------|----------------|-----------------|------------------------|--------------------|--------------------------|
| 107      | 78             | 4               | 625.0                  | 730.0              | 105.0                    |
| 108      | 83             | 4               | 1230.0                 | 1345.0             | 115.0                    |
| 128      | 978            | 22              | 1180.0                 | 1065.0             | 1325.0                   |
| 290      | 2694           | 14              | 1110.0                 | 150.0              | 9120.0                   |
| 401      | 1618           | 12              | 1290.0                 | 600.0              | 2190.0                   |

### Summary Statistics
| Metric | Mean | Min | 50% (Median) | Max |
|--------|------|-----|--------------|-----|
| Total Distance (km) | 348.9 | 1.0 | 82.0 | 4,260.0 |
| Number of Stops | 16.7 | 2 | 15 | 118 |
| Journey Duration (min) | 434.0 | 5.0 | 135.0 | 9,120.0 |

