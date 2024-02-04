import streamlit as st
from config import CONTRIBUTORS

def contributors_page():
    st.balloons()
    st.write(CONTRIBUTORS, unsafe_allow_html=True)