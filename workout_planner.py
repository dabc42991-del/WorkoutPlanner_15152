def calculate_bmi(weight, height):
    """Calculate BMI based on weight (kg) and height (cm)."""
    height_in_meters = height / 100  
    bmi = weight / (height_in_meters ** 2)
    return bmi

def suggest_workout(bmi):
    """Suggest a daily workout duration based on BMI."""
    if bmi < 18.5:
        return "Workout: Moderate exercises for 30 minutes."
    elif 18.5 <= bmi < 24.9:
        return "Workout: Regular exercise for 45 minutes."
    elif 25 <= bmi < 29.9:
        return "Workout: Intense exercises for 60 minutes."
    else:
        return "Workout: High-intensity exercises for 75 minutes."

def suggest_diet(bmi):
    """Suggest a basic diet plan based on BMI."""
    if bmi < 18.5:
        return "Diet: High-protein foods to gain weight."
    elif 18.5 <= bmi < 24.9:
        return "Diet: Balanced diet with moderate calories."
    elif 25 <= bmi < 29.9:
        return "Diet: Low-calorie diet to lose weight."
    else:
        return "Diet: Very low-calorie diet and consult a doctor."

def workout_planner():
    try:
        weight = input("Enter your weight (kg): ")
        height = input("Enter your height (cm): ")

        if not weight or not height:
            raise ValueError("Weight and height cannot be empty.")

        weight = float(weight)
        height = float(height)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        bmi = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")

        print(suggest_workout(bmi))
        print(suggest_diet(bmi))

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values.")

    except Exception as e:
        print(f"Unexpected error: {e}. Please try again.")

# Run the planner
workout_planner()
def calculate_bmi(weight, height):
    """Calculate BMI based on weight (kg) and height (cm)."""
    height_in_meters = height / 100  
    bmi = weight / (height_in_meters ** 2)
    return bmi

def suggest_workout(bmi):
    """Suggest a daily workout duration based on BMI."""
    if bmi < 18.5:
        return "Workout: Moderate exercises for 30 minutes."
    elif 18.5 <= bmi < 24.9:
        return "Workout: Regular exercise for 45 minutes."
    elif 25 <= bmi < 29.9:
        return "Workout: Intense exercises for 60 minutes."
    else:
        return "Workout: High-intensity exercises for 75 minutes."

def suggest_diet(bmi):
    """Suggest a basic diet plan based on BMI."""
    if bmi < 18.5:
        return "Diet: High-protein foods to gain weight."
    elif 18.5 <= bmi < 24.9:
        return "Diet: Balanced diet with moderate calories."
    elif 25 <= bmi < 29.9:
        return "Diet: Low-calorie diet to lose weight."
    else:
        return "Diet: Very low-calorie diet and consult a doctor."

def workout_planner():
    try:
        weight = input("Enter your weight (kg): ")
        height = input("Enter your height (cm): ")

        if not weight or not height:
            raise ValueError("Weight and height cannot be empty.")

        weight = float(weight)
        height = float(height)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        bmi = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")

        print(suggest_workout(bmi))
        print(suggest_diet(bmi))

    except ValueError as e:
        print(f"Error: {e}. Please enter valid numeric values.")

    except Exception as e:
        print(f"Unexpected error: {e}. Please try again.")

workout_planner()
