from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse

import numpy as np
import io

# ------------------------------------------------------------------------------

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Image Segmentation API"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")


# ------------------------------------------------------------------------------

img_height, img_width, n_classes = 256, 256, 8

def preprocess_image(file: UploadFile):
    """
    Prépare l'image envoyée par l'utilisateur (resize, normalisation)
    """
    pass

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint principal : reçoit une image, retourne un masque simulé.
    En mode test, on renvoie un masque réel fixe (test_mask.png)
    """
    print(f"Image reçue : {file.filename} — type : {file.content_type}")

    # Traitement image
    preprocessed_img = preprocess_image(file)

    # Le masque simulé
    mask_path = "tests/test_mask.npy"
    one_hot_mask = np.load(mask_path)

    # Transformer en classes
    mask_argmax = np.argmax(one_hot_mask, axis=-1)

    # Retour au format JSON-compatible
    return JSONResponse(content={"mask": mask_argmax.tolist()})
