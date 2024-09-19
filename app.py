import pickle
import requests
import streamlit as st 
from multiapp import MultiApp
from apps import home, about, contact

with open('E:\\ML PROJECTS\\my_streamlit_app\\apps\\style.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)
    
app=MultiApp()

app.add_app("Home", home.app)
app.add_app("Recommendations", contact.app)
app.add_app("About", about.app)

app.run()
