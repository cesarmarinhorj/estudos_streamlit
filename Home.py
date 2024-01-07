import streamlit as st

home = open('./home.md', 'r')
st.markdown(home.read(), unsafe_allow_html=False)
