import pickle

def load_model():
    with open("assets/model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# No st.slider or other UI elements here!