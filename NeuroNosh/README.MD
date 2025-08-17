🌈 NeuroNosh: Mood-Aware Recipe Generator for Neurodiverse Individuals


Recipes that understand your sensory needs and emotional state

🌟 Why NeuroNosh?
Neurodiverse individuals often face unique challenges with food: sensory sensitivities, emotional regulation needs, and overwhelming recipe choices. NeuroNosh solves this by generating personalized recipes that consider:

🧠 Sensory preferences (texture, temperature, sound sensitivity)
😌 Current emotional state (anxious, overwhelmed, low energy)
🥄 Practical constraints (cooking skill, available tools, time)
🌈 Neurodiverse-friendly presentation (clear instructions, visual aids, reduced cognitive load)
"Finally a recipe app that doesn't assume I can handle loud kitchen sounds or mushy textures!"
- Alex, autistic developer and beta tester 

✨ Key Features
Mood Detection
Simple emoji-based mood input instead of complex forms
FastAPI endpoint with sentiment analysis
Sensory Filters
Customizable texture, sound, visual, and smell preferences
Pydantic models with neurodiverse-specific validators
Step Simplification
Breaks recipes into micro-steps with sensory warnings
NLP processing with spaCy
Visual Recipe Cards
Clean layout with color-coded steps and sensory icons
Jinja2 templates with WCAG-compliant colors
Crisis Mode
Emergency "I need food NOW" with 3-ingredient options
Priority queue algorithm

🚀 Quick Start
Prerequisites
Python 3.9+
Pipenv (recommended)
Installation
bash


1
2
3
4
5
6
7
8
9
10
# Clone the repository
git clone https://github.com/yourusername/NeuroNosh.git
cd NeuroNosh

# Set up environment (Pipenv)
pipenv install
pipenv shell

# Run the server
uvicorn main:app --reload --port 8000
First-Time Configuration
Create .env file:

ini


1
2
3
# Sensory defaults for neurodiverse users
DEFAULT_SENSORY_PROFILE='{"textures": ["crunchy", "firm"], "avoid_sounds": ["blender", "frying"]}'
MOOD_EMOJI_MAP='{"😊": "calm", "😰": "anxious", "😴": "low_energy"}'
🌈 Sample Workflow
Set your mood

Configure sensory needs
python


1
2
3
4
5
6
7
8
9
10
⌄
⌄
# API request example
POST /recipes
{
  "mood": "anxious",
  "sensory_preferences": {
    "max_noise_level": "quiet",
    "avoid_textures": ["slimy", "gritty"],
    "preferred_temperatures": ["warm"]
  }
}
Receive neuro-inclusive recipe


Notice: Sensory warnings, step duration estimates, and alternative tools
🌐 API Endpoints
/recipes
POST
Generate personalized recipes
Sensory filter validation
/mood-profile
GET
Get mood-recipe correlations
Anonymized neurodiverse dataset
/sensory-guide
GET
Sensory substitution database
Community-sourced alternatives
/crisis-mode
POST
Emergency quick meals
3-ingredient guarantee
/recipe/{id}/simplify
PATCH
Break steps into micro-tasks
Cognitive load reduction

🌱 Contributing
We actively seek contributions from neurodiverse developers and allies:

Sensory Testing - Help validate our sensory preference models
Recipe Expansion - Contribute neurodiverse-friendly recipes
Accessibility Audits - Improve our WCAG compliance
Mood Dataset - Anonymously share mood/food correlations
Contribution Guidelines:

All PRs require sensory impact assessment
Documentation must include alt-text for images
Color contrast must meet AA standards
No "just try harder" language in comments
SVG content

🌈 Design Philosophy
NeuroNosh follows these neuro-inclusive principles:

✨ "Nothing about us without us" - All features co-designed with neurodiverse testers
🌈 Sensory-first design - Prioritizes reducing overwhelm over visual flair
⏱️ Cognitive budgeting - Never asks for more than 3 decisions at once
🌻 Error kindness - "Oops" instead of "Error" with clear recovery paths 

📜 License
Distributed under MIT License. Special clause:
All derivative works must maintain neurodiverse accessibility features and cannot implement paywalls for sensory filters.

"NeuroNosh didn't just give me dinner - it gave me back kitchen confidence after years of food anxiety."
- Jamie, ADHD chef and community tester 

Contribute to NeuroNosh

Sensory Safe

Ready to cook without compromise?
👉 Launch NeuroNosh Demo 👈
Hosted on neurodiverse-friendly infrastructure (low-latency, no autoplay media)

