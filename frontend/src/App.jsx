import React, { useState } from 'react';
import './App.css';

function App() {
  const [ticker, setTicker] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleInputChange = (event) => {
    setTicker(event.target.value);
  };

  const getPrediction = () => {
    // Placeholder for API call (we'll implement this later)
    const dummyPrediction = 1; // Dummy prediction
    setPrediction(dummyPrediction);
  };

  return (
    <div className="App">
      <h1>Stock Prediction</h1>
      <label htmlFor="ticker">Enter Stock Ticker:</label>
      <input
        type="text"
        id="ticker"
        name="ticker"
        value={ticker}
        onChange={handleInputChange}
      />
      <button onClick={getPrediction}>Predict</button>
      <div id="predictionResult">
        {prediction !== null ? (
          <p>Prediction for {ticker}: {prediction}</p>
        ) : (
          <p>Enter a ticker and click 'Predict'</p>
        )}
      </div>
    </div>
  );
}

export default App;