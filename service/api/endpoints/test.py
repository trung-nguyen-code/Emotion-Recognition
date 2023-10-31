import numpy as np
from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO

test_router = APIRouter()


@test_router.post("/test/")
def test(im: UploadFile):
    if im.file.split(".")[-1] in ("jpg", "jpeg", "png"):
        pass
    else:
        raise HTTPException(status_code=442, detail="Not an image")
    image = Image.open(BytesIO(im.file.read()))
    image = np.array(image)

    return emo_detect(image)
