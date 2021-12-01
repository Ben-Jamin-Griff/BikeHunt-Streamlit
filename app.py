import streamlit as st
from PIL import Image
import requests
import json

def make_request(uploaded_file, bytes_data):
    url = "https://bikehuntapi.herokuapp.com/api/predict"
    payload={}
    files=[('file',(uploaded_file.name,bytes_data,'image/jpeg'))]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response

st.title("BikeHunt 🚵‍♂️ Early Demo")
st.subheader("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image)
    bytes_data = uploaded_file.getvalue()
    prediction = make_request(uploaded_file, bytes_data)
    result = json.loads(prediction.text)
    st.subheader("Bike Type: " + result["prediction"])