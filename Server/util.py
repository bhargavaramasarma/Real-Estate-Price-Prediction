import json, pickle
import numpy as np
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    n = np.zeros(len(__data_columns))
    n[0]=sqft
    n[1]=bath
    n[2]=bhk
    if loc_index >= 0:
        n[loc_index] = 1
    return round(__model.predict([n])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("/home/bhargav-sarma/Bhargav/AIML/Real Estate Price Prediction/Server/artifacts/columns.json", 'r') as f:
        __data_columns= json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
    with open("/home/bhargav-sarma/Bhargav/AIML/Real Estate Price Prediction/Server/artifacts/bangalore_home_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))