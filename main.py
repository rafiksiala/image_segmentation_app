from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
from fastapi.responses import FileResponse

import numpy as np
from PIL import Image

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

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint principal : reçoit une image, retourne un masque simulé.
    En mode test, on renvoie un masque réel fixe (test_mask.png)
    """
    print(f"Image reçue : {file.filename} — type : {file.content_type}")

    # Traitement image
    image = preprocess_image(file)

    mask_path = "tests/test_mask.png"  # Le masque simulé

    mask = Image.open(mask_path).resize((img_width, img_height))
    mask = np.array(mask).astype(np.uint8)

    # Retour au format JSON-compatible
    return JSONResponse(content={"mask": mask.tolist()})
