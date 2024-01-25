import streamlit as st
import requests

def predict_image(image):
    url = 'https://srastog-alzheimer-detection.hf.space/predict'
    files = {'file': image}
    headers = {'accept': 'application/json'}

    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  # Check for HTTP errors

        result = response.json()
        return result
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.error(f"An unexpected error occurred: {err}")
    except ValueError as ve:
        st.error(f"Error decoding JSON: {ve}")

    return None


def main():

    st.title("NeuroNetAI")
    st.subheader("Using Machine Learning for Alzheimer's Disease detection")
    st.write("Please upload an image to be classified")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write("The image was sent to the backend. You can see the response we got back below.")

        # Make prediction using the provided function
        result = predict_image(uploaded_file)

        if result is not None:
            # Display the result
            st.subheader("Prediction Result:")
            st.write(f"Label: {result['label']}")
            st.write(f"Probability: {(result['probability'] * 100):.2f}%")

if __name__ == "__main__":
    main()
