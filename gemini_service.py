from app.gemini_generator import generate_workout
from app.nutrition import generate_nutrition, generate_tip
from app.updated_plan import update_workout


def generate_plan(name, age, gender, height, weight, goal, activity_level, days, equipment):
    return generate_workout(name, age, weight, goal, activity_level)
