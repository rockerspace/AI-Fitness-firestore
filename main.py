# main.py or app.py (depending on your app's structure)

from save_session import save_session # Import the save function

def on_exercise_finished(exercise_name, duration):
    # Example trigger: when exercise is detected as completed
    print(f"Exercise {exercise_name} completed!")
    save_session(exercise_name, duration)  # Call the function to save data

# Sample scenario where exercise is detected
exercise_name = "Push-Up"
duration = 120  # Assume 120 seconds for the exercise

on_exercise_finished(exercise_name, duration)
