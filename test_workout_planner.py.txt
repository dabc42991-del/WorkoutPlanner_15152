%%writefile test_workout_planner.py
from workout_planner import calculate_bmi, suggest_workout

def test_calculate_bmi():
    bmi = calculate_bmi(70, 175)
    assert round(bmi, 2) == 22.86

def test_suggest_workout():
    assert suggest_workout(27.0) == "Workout: Intense exercises for 60 minutes."
