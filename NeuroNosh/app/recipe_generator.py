def generate_recipe(mood: str, sensory_input: str, diet: str):
    # Very basic logic for now
    if mood == "anxious":
        return "Chamomile tea with soft banana oat cookies"
    elif mood == "calm":
        return "Light vegetable soup with rice"
    else:
        return "Mood not recognized – try again"
