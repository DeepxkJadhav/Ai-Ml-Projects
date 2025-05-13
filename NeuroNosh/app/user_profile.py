class UserProfile:
    def __init__(self, allergies=[], preferences=[]):
        self.allergies = allergies
        self.preferences = preferences

    def update_profile(self, new_allergies, new_preferences):
        self.allergies = new_allergies
        self.preferences = new_preferences
