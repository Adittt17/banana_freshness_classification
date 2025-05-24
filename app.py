import streamlit as st
from PIL import Image
import numpy as np
import os
import tempfile
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Judul
st.title("🍌 Klasifikasi Pisang Segar vs Busuk")

# Load model dari lokal
model = load_model("banana_asli.h5")  # Ganti dengan path lokal model kamu

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar pisang...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Gambar Diupload', use_column_width=True)

    # Preprocessing
    img = img.resize((150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    # Prediksi
    preds = model.predict(x)
    label = "🍌 Fresh Banana (Segar)" if preds[0][0] < 0.5 else "🤢 Rotten Banana (Busuk)"
    confidence = (1 - preds[0][0]) if preds[0][0] < 0.5 else preds[0][0]

    # Tampilkan hasil
    st.markdown(f"### Prediksi: {label}")
    st.markdown(f"**Confidence Score:** {confidence:.2%}")
