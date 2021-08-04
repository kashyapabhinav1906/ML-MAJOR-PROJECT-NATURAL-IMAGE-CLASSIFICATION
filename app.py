import streamlit as st 
from PIL import Image
import classify 
import numpy as np


st.title("Natural_Image_Classifier")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:

        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        st.write("")

        if st.button('predict'):
                st.markdown("# RESULT")
                label = classify.predict(image)
                # label = label.items()

                # res = sign_names.get(label)
                res=label
                for i in res:
                    st.markdown(i+" : "+str(res[i]) +"%")
