import streamlit as st
import joblib
import numpy as np
from PIL import Image
from tensorflow import keras

st.set_page_config(page_title="MNIST Digit Classifier", page_icon="🔢")

@st.cache_resource
def load_models():
    return (
        joblib.load("perceptron.pkl"),
        keras.models.load_model("ANN.keras"),
        keras.models.load_model("CNN.keras")
    )

perceptron, ann, cnn = load_models()

perceptron, ann, cnn = load_models()



st.title("🔢 MNIST Digit Classifier")
st.write("Compare Perceptron, ANN and CNN.")

model_name = st.selectbox(
    "Choose Model",
    ["Perceptron", "ANN", "CNN"]
)

file = st.file_uploader(
    "Upload a handwritten digit",
    type=["png", "jpg", "jpeg"]
)

if file:
    image = Image.open(file).convert("L")
    st.image(image, width=200)

    image = image.resize((28, 28))
    x = np.array(image).astype("float32") / 255.0
    
    st.image(x, caption="Processed Image", width=200)

if st.button("Predict"):

    if model_name == "Perceptron":
        pred = perceptron.predict(x.reshape(1, 28, 28), verbose=0)
        digit = np.argmax(pred[0])

    elif model_name == "ANN":
        pred = ann.predict(x.reshape(1, 28, 28), verbose=0)
        digit = np.argmax(pred[0])

    else:
        pred = cnn.predict(x.reshape(1, 28, 28, 1), verbose=0)
        digit = np.argmax(pred[0])

    st.success(f"Predicted Digit: {digit}")