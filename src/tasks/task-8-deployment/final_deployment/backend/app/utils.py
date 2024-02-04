import numpy as np
import os
from tensorflow import keras


def classify_img(model,img):

    # Assuming img is a numpy array
    img = np.asarray(img)
    # rescaling in case it's not in 0-1 scale
    if img.max() > 1:
        img = img / 255.0
    # Convert to tensor and add an extra dimension
    img = np.expand_dims(img, axis=0)

    # new keras version
    pred = model.predict(img)
    print("pred:", pred)
    pred_pct = pred[0][np.argmax(pred)]
    return np.argmax(pred), pred_pct




def get_alzheimer_model():
    model_path = os.path.join(os.path.dirname(__file__), 'model_1.h5')
    params_path = os.path.join(os.path.dirname(__file__), 'best_model_custom_1.h5')

    model = keras.models.load_model(model_path)
    model.load_weights(params_path)

    # # Show the model architecture
    # model.summary()
    return model

