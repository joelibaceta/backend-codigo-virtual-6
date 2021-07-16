from flask import Flask
from flask import request
from flask import render_template
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    file = request.files["image"]
    file.save("temp.jpg")

    im = Image.open("temp.jpg")
    im = im.resize((28, 28))

    im.save('output_28_28.jpg')

    pixels = []
    for j in range(0, 28):
        row = []
        for i in range(0, 28):
            row.append(max(im.getpixel((i, j))))
        pixels.append(row)

    px = np.asarray(pixels, dtype='float32')
    px = px.reshape((1, 28, 28, 1))

    model = tf.keras.models.load_model('mnist_model.h5')
    print(px.shape)
    prediction = model.predict(px)[0]

    print(prediction)
    
    return str(np.argmax(prediction))

