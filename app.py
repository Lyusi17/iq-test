from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

model = tf.keras.models.load_model("emotion_model.keras")

classes = ["Angry", "Fear", "Happy", "Sad", "Surprise"]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    image = image.resize((48, 48))

    image = np.array(image) / 255.0

    image = np.expand_dims(image, axis=0)

    pred = model.predict(image)

    emotion = classes[np.argmax(pred)]

    return {"emotion": emotion}