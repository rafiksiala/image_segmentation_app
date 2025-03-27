import streamlit as st
import requests
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# FastAPI tourne en interne sur `127.0.0.1:8001`
API_URL = "http://127.0.0.1:8001/predict/"

st.set_page_config(page_title="Segmentation d'image", layout="centered")
st.title("Segmentation d'images")
st.write("Upload une image pour visualiser le masque segmenté prédit par l'API.")

# Upload de l'image
uploaded_file = st.file_uploader("Upload une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Affichage de l’image originale
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Image originale")

    # Rewind du fichier avant envoi
    uploaded_file.seek(0)

    # Construction de la requête multipart pour FastAPI
    files = {
        "file": (uploaded_file.name, uploaded_file.read(), uploaded_file.type)
    }

    # Appel API
    with st.spinner("Envoi à l'API FastAPI..."):
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        st.success("Prédiction reçue !")
        mask = np.array(response.json()["mask"])

        # Affichage du masque prédit
        st.write("Masque prédit :")
        fig, ax = plt.subplots()
        ax.imshow(mask, cmap="tab10", vmin=0, vmax=7)
        ax.axis("off")
        st.pyplot(fig)

    else:
        st.error(f"Erreur API : {response.status_code}")
        st.text(response.text)
