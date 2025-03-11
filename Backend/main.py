from flask import request, jsonify
from config import app, db
from models import Prediction

@app.route('/predict', methods=['GET'])
def predict():
    ticker = request.args.get('ticker')

    # Dummy prediction for now
    prediction = 1  # Or 0, or random

    # Store the prediction in the database
    new_prediction = Prediction(ticker=ticker, prediction=prediction)
    db.session.add(new_prediction)
    db.session.commit()

    return jsonify({'ticker': ticker, 'prediction': prediction})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)