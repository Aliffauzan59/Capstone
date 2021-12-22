from flask import Flask, render_template,request
import cv2
import numpy as np
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image


app = Flask(__name__)

MODEL_PATH = 'model_final.h5'
model = MODEL_PATH
print("+"*50, "Model is loaded")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def prediction():

    img = request.files['img']

    img.save("img.jpg")

    image = cv2.imread("img.jpg")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = cv2.resize(image, (224,224))

    image = np.reshape(image, (1,224,224,3))

    pred = model.predict(image)

    pred = np.argmax(pred)


    return render_template("base.html", data=pred)


if __name__ == "__main__":
    app.run(debug=True)

