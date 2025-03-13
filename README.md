# Real Estate Price Prediction

This is a basic machine learning project that predicts the price of homes in Bengaluru, India. The model is trained on historical housing data and considers factors such as area, number of bedrooms, and number of bathrooms to estimate the price in lakh rupees.

## Project Structure
```
├── Client
│   ├── app.css
│   ├── app.html
│   └── app.js
├── Model
│   ├── bangalore_home_prices_model.pickle
│   ├── bhp.ipynb
│   └── columns.json
├── Server
│   ├── artifacts
│   │   ├── bangalore_home_prices_model.pickle
│   │   └── columns.json
│   ├── server.py
│   └── util.py
└── bengaluru_house_prices.csv
```

## How It Works
1. The model is trained using historical data from Bengaluru housing prices.
2. Input features include:
   - Area (square feet)
   - Number of Bedrooms (BHK)
   - Number of Bathrooms
3. The model outputs the predicted price in lakh rupees.

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/your-username/real-estate-price-prediction.git
cd real-estate-price-prediction
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the server:
```bash
python server.py
```
4. Access the web app at:
```
http://localhost:5000/
```

## Usage
- Enter the area, number of bedrooms, and bathrooms in the web app.
- Click on "Predict" to get the estimated price.

## Dataset
The dataset used for training contains past Bengaluru housing prices.

## Future Improvements
- Add more features for better accuracy.
- Integrate different machine learning models.
- Improve frontend UI.

## Author
[Bhargav Sarma](https://github.com/bhargavaramasarma)

---
Feel free to contribute or raise issues if you find any bugs or want to suggest improvements!

