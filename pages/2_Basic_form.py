import streamlit as st

colors = ['red','orange','green','blue','violet']

st.title("Basic")
with st.form("form1"):
   st.write("Inside the form")
   my_number = st.slider('Pick a number', 1, 10)
   my_color = st.selectbox('Pick a color', colors)
   st.form_submit_button('Submit my picks')

# This is outside the form
st.write(my_number)
st.write(my_color)