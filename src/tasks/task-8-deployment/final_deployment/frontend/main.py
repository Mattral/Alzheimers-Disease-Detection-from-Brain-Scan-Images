import base64
import streamlit as st

from config import *
from _model import model_page 
from _contributors import contributors_page 

st.set_page_config(
    page_title=f"Omdena | Toronto Chapter",
    page_icon="🍁",
    initial_sidebar_state="expanded"
)

def set_page_background(png_file):
    @st.cache_data()
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    bin_str = get_base64_of_bin_file(png_file)
    custom_css = f'''
        <style>
            .stApp {{
                background-image: url("data:image/png;base64,{bin_str}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: scroll;
            }}
            
            #MainMenu {{visibility: hidden;}}

            footer {{visibility: hidden;}}
            icon {{color: white;}}
            nav-link {{--hover-color: grey; }}
            nav-link-selected {{background-color: #4ABF7E;}}
        </style>
    '''
    st.markdown(custom_css, unsafe_allow_html=True)

set_page_background('assets/background.webp')
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)

def home_page():
    st.write("# Early Detection and Diagnosis of Alzheimer's Disease through Brain Scan Analysis", unsafe_allow_html=True)
    st.image(IMG_BANNER)

    st.write(PROJECT_PROBLEM, unsafe_allow_html=True)
    st.write(PROJECT_BACKGROUND, unsafe_allow_html=True)
    
    left, right = st.columns(2)
    
    with left:
        st.write(PROJECT_GOALS, unsafe_allow_html=True)
    
    with right:
        st.write(PROJECT_TIMELINE, unsafe_allow_html=True)

def main():
    st.sidebar.image("assets/logo.png")
    st.sidebar.write(SIDEBAR_TEXT_1, unsafe_allow_html=True)
    selected_task = st.sidebar.selectbox("Please navigate through the different sections of our website from here", ["Home", "About", "Visualization", "Model", "Contributors"], label_visibility="hidden")
    st.sidebar.write(SIDEBAR_TEXT_2, unsafe_allow_html=True)
    
    if selected_task == "Home":
        home_page()
    elif selected_task == "About":
        st.write(ABOUT_US, unsafe_allow_html=True)
    elif selected_task == "Visualization":
        st.write(VISUALIZATION, unsafe_allow_html=True)
    elif selected_task == "Model":
        model_page()
    elif selected_task == "Contributors":
        contributors_page()
    
if __name__ == "__main__":
    main()