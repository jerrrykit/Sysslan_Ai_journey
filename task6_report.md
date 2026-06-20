# Task 6: Final Interactive Machine Learning Project

## Task 6.1: Interactive ML System

For the final task of this project, an end-to-end interactive system was developed using Python. 

The system (`task6.py`) provides a Command-Line Interface (CLI) that allows users to interact directly with the best-performing predictive model from Task 5 (the Random Forest Regressor).

### Features of the Interactive System:
1. **Live Model Training:** The system initializes by loading the processed dataset and instantly training the Random Forest Regressor model on the fly.
2. **User Input:** It prompts the user for real-world journey details:
   - `Total Distance`
   - `Number of Stops`
   - `Start Departure Minute`
   - `End Arrival Minute`
3. **Instant Prediction:** The model processes the input and immediately outputs the predicted journey duration in minutes.
4. **Dynamic Visualization:** 
   - A baseline visualization (`interactive_base.png`) is generated showing the historical test data's predicted vs. actual values.
   - If the user knows the *actual* duration of the journey they inputted, the system asks for it. It will then dynamically update the scatter plot (`interactive_user_prediction.png`) with a **prominent red dot** representing the user's specific journey compared against the historical data. This visually demonstrates how the model's prediction for the new data point aligns with its general performance.
5. **Continuous Loop:** The system allows for multiple predictions back-to-back until the user chooses to exit.

### How to Run
To use the interactive system, open your terminal, navigate to the project directory, and run:
```bash
python task6.py
```
