import cv2
import numpy as np
import onnxruntime as rt
import time

IMG_SIZE = 256
output_path = "/home/trung/neuralearn/service/core/logic/eff.onnx"


def emotion_detector(img_array):
    # image = cv2.imread(/)
    time_init = time.time()
    if len(img_array.shape) == 2:
        img_array = cv2.cvtColor(img_array, cv2.COLOR_GRAY2BGR)
    image = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    image = np.expand_dims(image, axis=0)

    providers = ["CPUExecutionProvider"]
    m = rt.InferenceSession(output_path, providers=providers)
    loading_time = time.time() - time_init
    print("---->", m)
    onnx_pred = m.run(["dense_2"], {"onnx": image})
    time_elapsed = time.time() - time_init

    print(np.argmax(onnx_pred[0][0]))

    emotion = None
    if np.argmax(onnx_pred[0][0]) == 0:
        emotion = "angry"
    elif np.argmax(onnx_pred[0][0]) == 1:
        emotion = "happy"
    else:
        emotion = "sad"

    return {"emotion": emotion, "time_elapsed": time_elapsed}
