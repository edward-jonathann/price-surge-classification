import pickle

def load_encoders():
    with open("assets/encoders.pkl", "rb") as file:
        encoders = pickle.load(file)
    return encoders