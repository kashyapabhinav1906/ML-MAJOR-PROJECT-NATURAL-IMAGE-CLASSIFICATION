from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
 
import streamlit as st

@st.cache(allow_output_mutation=True)
def get_model():
        model = load_model('Model/cifar10_02.h5')
        print('Model Loaded')
        return model 

classes = ['AIRPLANE', 'AUTOMOBILE', 'BIRD', 'CAT',
           'DEER', 'DOG', 'FROG', 'HORSE', 'SHIP', 'TRUCK']
def predict(img):
    cifar10_model=get_model()
    img = img.resize((32, 32), Image.ANTIALIAS)
    img = img.convert('RGB')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.
    preds = cifar10_model.predict(x)[0]
    return {classes[x]: float(preds[x]*100) for x in np.argsort(preds)[::-1][:3]}
    # return classes[np.argsort(preds)[-1]]
    
