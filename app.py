import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Title
st.title("🍌 Fresh vs Rotten Banana Classification")

# Load model from local
model = load_model("banana_asli.h5")  # Replace with your local model path

# Upload image
uploaded_file = st.file_uploader("Upload a banana image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Preprocessing
    img = img.resize((150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    # Prediction
    preds = model.predict(x)
    label = "🍌 Fresh Banana" if preds[0][0] < 0.5 else "🤢 Rotten Banana"
    confidence = (1 - preds[0][0]) if preds[0][0] < 0.5 else preds[0][0]

    # Display results
    st.markdown(f"### Prediction: {label}")
    st.markdown(f"**Confidence Score:** {confidence:.2%}")
