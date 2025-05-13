from fastapi import FastAPI
from app.mood_detector import get_mood
from app.recipe_generator import generate_recipe

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to MoodMealAI"}

@app.get("/generate/")
def get_recipe(mood: str, sensory_input: str, diet: str):
    recipe = generate_recipe(mood, sensory_input, diet)
    return {"recipe": recipe}
