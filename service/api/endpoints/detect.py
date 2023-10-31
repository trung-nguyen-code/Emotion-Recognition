import numpy as np
from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
from core.logic.onnx_inference import emotion_detector
from core.schemas.output import APIOutput

emo_router = APIRouter()


@emo_router.post("/detect/", response_model=APIOutput)
def detect(im: UploadFile):
    if im.filename.split(".")[-1] in ("jpg", "jpeg", "png"):
        pass
    else:
        raise HTTPException(status_code=442, detail="Not an image")
    image = Image.open(BytesIO(im.file.read()))
    image = np.array(image)
    image = image.astype("float32")

    return emotion_detector(image)
