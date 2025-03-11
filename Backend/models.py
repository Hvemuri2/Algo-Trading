from config import db

# This file includes the code to commnicate with our database.

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10))
    prediction = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "ticker": self.prediction,
            "prediction": self.prediction,
        }
