# src/brain.py
from sklearn.ensemble import RandomForestClassifier
import joblib

class AntBotPi:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        self.model.fit(X, y)
        print("AntBotPi a fini son apprentissage !")

    def predict(self, data):
        return self.model.predict(data)

    def save_model(self, path="models/antbot.pkl"):
        joblib.dump(self.model, path)
