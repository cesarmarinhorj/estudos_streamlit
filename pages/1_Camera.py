import streamlit as st

st.title('Picture')
with st.form('controls'):
    picture = st.camera_input("Take a picture")
    st.form_submit_button('show')

    if picture:
        st.image(picture)
