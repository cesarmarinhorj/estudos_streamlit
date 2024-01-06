import streamlit as st

def sum(a,b):
    return a+b

col1,col2 = st.columns([1,2])
col1.title('Sum')
with st.form('addition'):
    a = st.number_input('a')
    b = st.number_input('b')
    submit = st.form_submit_button('add')

if submit:
    col2.title(f'{sum(a,b):.2f}')

