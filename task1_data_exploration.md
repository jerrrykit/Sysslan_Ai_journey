# Task 1: Understanding the Data

## Task 1.1: Dataset Overview
- **Total records:** 186,074
- **Total columns:** 12
- **Columns:** `SN`, `Train_No`, `Station_Code`, `1A`, `2A`, `3A`, `SL`, `Station_Name`, `Route_Number`, `Arrival_time`, `Departure_Time`, `Distance`

## Task 1.2: Train-wise Starting and Ending Stations
Here is a sample showing the starting and ending stations for the first 10 trains:

| Train_No | Starting_Station | Ending_Station |
|----------|------------------|----------------|
| 107 | SAWANTWADI R | MADGOAN JN. |
| 108 | MADGOAN JN. | SAWANTWADI R |
| 128 | MADGOAN JN. | CHHATRAPATI |
| 290 | DELHI-SAFDAR | DELHI-SAFDAR |
| 401 | AURANGABAD | VARANASI JN. |
| 421 | LUCKNOW JN. | SHRI MATA VA |
| 422 | SHRI MATA VA | LUCKNOW JN. |
| 477 | SIRSA | SIRSA |
| 502 | RAJENDRANAGA | AMBALA CANTT |
| 504 | PATNA JN. | BATHINDA JN |

## Task 1.3: Basic Statistics
Based on the aggregated data per train (total distance and number of stops):

**Distance Statistics:**
- Count: 11,113 trains
- Mean Distance: 348.87 km
- Max Distance: 4,260.0 km
- Median Distance: 82.0 km
- Standard Deviation: 596.18 km

**Stops Statistics:**
- Mean Number of Stops: 16.75
- Max Stops: 118
- Median Stops: 15

## Task 1.4: Data Quality Assessment
- **Missing Values:** No missing values were found in any column (0 missing in all 12 columns).
- **Duplicate Rows:** 0 duplicate rows found.
- **Incorrect Values:** Checked for negative distances (0 instances) and non-positive stop numbers (0 instances). The data quality appears very clean.

