from fastapi import FastAPI
from fastapi.responses import FileResponse

# ------------------------------------------------------------------------------

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Image Segmentation API"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")
