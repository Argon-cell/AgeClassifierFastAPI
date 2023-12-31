import requests
from PIL import Image
import re
import validators
from io import BytesIO
import torch
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from transformers import ViTFeatureExtractor, ViTForImageClassification

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/get-age-by-photo")
async def get_image(url):
    if validators.url(url) is True:
        im = Image.open(requests.get(url, stream=True).raw)
        print(im)

        # Init model, transforms
        model = ViTForImageClassification.from_pretrained('nateraw/vit-age-classifier')
        transforms = ViTFeatureExtractor.from_pretrained('nateraw/vit-age-classifier')

        # Transform our image and pass it through the model
        inputs = transforms(im, return_tensors='pt')
        output = model(**inputs)

        # Predicted Class probabilities
        proba = output.logits.softmax(1)

        # Predicted Classes
        preds = proba.argmax(1)
        imgplot = plt.imshow(im)
        plt.show()
        a = {'0': "0-2", '1': "3-9", '2':  "10-19", '3': "20-29", '4': "30-39", '5': "40-49", '6': "50-59", '7': "60-69", '8': "more than 70"}
        number = re.findall(r'\d+', str(preds[0]))
        result = a[number[0]]
        
        return {"Age": result}
    else:
        return {"Age": "This is not url"}


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8000)