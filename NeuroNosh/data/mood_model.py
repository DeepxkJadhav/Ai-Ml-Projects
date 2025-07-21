# mood_model.py

import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from torchvision import transforms
from PIL import Image
import torch.nn.functional as F

class MoodModel:
    def __init__(self, mode='text'):
        self.mode = mode.lower()

        if self.mode == 'text':
            self._load_text_model()
        elif self.mode == 'image':
            self._load_image_model()
        else:
            raise ValueError("Unsupported mode. Choose 'text' or 'image'.")

    def _load_text_model(self):
        # Load a sentiment analysis model (can be customized)
        model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def _load_image_model(self):
        # Load a simple facial emotion model (example - replace with custom)
        # NOTE: You need to download or train a facial emotion recognition model
        from fer import FER
        self.detector = FER(mtcnn=True)

    def predict_text_mood(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        probs = F.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(probs).item()

        # Custom mapping based on model class labels
        mood_map = {
            0: "Very Negative",
            1: "Negative",
            2: "Neutral",
            3: "Positive",
            4: "Very Positive"
        }
        return mood_map.get(predicted_class, "Unknown")

    def predict_image_mood(self, image_path: str):
        image = Image.open(image_path)
        result = self.detector.detect_emotions(image)

        if not result:
            return "No face detected"
        top_emotion = max(result[0]['emotions'], key=result[0]['emotions'].get)
        return top_emotion

    def predict(self, input_data):
        if self.mode == 'text':
            return self.predict_text_mood(input_data)
        elif self.mode == 'image':
            return self.predict_image_mood(input_data)

# Example usage
if __name__ == "__main__":
    text_model = MoodModel(mode='text')
    print("Text Mood:", text_model.predict("I'm feeling really happy and energetic today!"))

    image_model = MoodModel(mode='image')
    print("Image Mood:", image_model.predict("sample_face.jpg"))
