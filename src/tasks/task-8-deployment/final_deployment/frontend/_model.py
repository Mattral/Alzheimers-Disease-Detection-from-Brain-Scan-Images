import requests
import streamlit as st
from config import API_URL, CLASS_LABELS

def model_page():
    st.write("#### Upload brain x-ray image here...")
    uploaded_file = st.file_uploader("Upload brain x-ray image here...", type=["jpg", "png", "jpeg"], label_visibility="hidden")
    predict_button = st.button("ㅤㅤPredictㅤㅤ")

    if predict_button and uploaded_file:
        result_ele = st.empty()
        result_ele.write("Processing...")
        st.image(uploaded_file, use_column_width=True)
        result = predict_image(uploaded_file)   
        label = CLASS_LABELS[int(result['label'])]
        prob = round(result['probability'], 4)*100
        
        result_ele.info(f"""According to our diagnosis, there is a **{prob}%** chance that you are **{label}**.""")
        st.toast("Prediction completed!", icon="🎉")
        
    elif predict_button and not uploaded_file:
        st.toast("Please upload an image first!", icon="⚠️")
            
def predict_image(image):
    files = {'file': image}
    headers = {'accept': 'application/json'}

    try:
        response = requests.post(API_URL, headers=headers, files=files)
        response.raise_for_status()

        result = response.json()
        return result
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

    return None