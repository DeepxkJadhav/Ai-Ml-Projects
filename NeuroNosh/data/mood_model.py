# recipe_model.py

import csv
import random

class RecipeModel:
    def __init__(self, csv_file='recipes.csv'):
        self.recipes = self._load_recipes(csv_file)

    def _load_recipes(self, file_path):
        recipes = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    recipes.append({
                        "name": row["name"],
                        "type": row["type"],
                        "diet": row["diet"],
                        "mood": row["mood"],
                        "cuisine": row["cuisine"],
                        "ingredients": row["ingredients"],
                        "instructions": row["instructions"]
                    })
        except FileNotFoundError:
            print("Error: CSV file not found.")
        return recipes

    def recommend_recipe(self, mood, diet=None, cuisine=None):
        mood = mood.capitalize()
        filtered = [r for r in self.recipes if r["mood"] == mood]

        if diet:
            filtered = [r for r in filtered if r["diet"].lower() == diet.lower()]

        if cuisine:
            filtered = [r for r in filtered if r["cuisine"].lower() == cuisine.lower()]

        if not filtered:
            return "No matching recipes found."

        return random.choice(filtered)

# Example usage
if __name__ == "__main__":
    model = RecipeModel()
    mood_input = "Sad"
    recipe = model.recommend_recipe(mood_input, diet="veg")
    
    if isinstance(recipe, dict):
        print(f"Recommended Recipe for Mood '{mood_input}':")
        print(f"Name: {recipe['name']}")
        print(f"Type: {recipe['type']}")
        print(f"Cuisine: {recipe['cuisine']}")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Instructions: {recipe['instructions']}")
    else:
        print(recipe)
