import datetime
import streamlit as st

col1,col2 = st.columns([1,2])
col1.title('Terms')

location = ['Suburb','Center','Interior']
size = ['Small','Medium','Large']
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
marks = ['Bad', 'Not So Bad', 'Not Good', 'Good', 'Very Good', 'Nice job']

with st.form('controls'):
    agree = st.checkbox('Agree with terms?')
    # st.button('Click')
    st.radio('Where you live?', location, horizontal=True)
    st.selectbox('Pick your gender', size)
    st.multiselect('choose a planet', planets)
    mark = st.select_slider('Pick a mark', marks)
    num = st.slider('Pick a number', 0, 10)
    feature = st.toggle('Activate feature')
    dts = st.date_input("Start date", datetime.date(2024, 1, 1))
    dtf = st.date_input("Finish date", datetime.date(2024, 1, 31))
    t = st.time_input('Set an alarm for', datetime.time(8, 45))

    st.form_submit_button('show')

    if agree:
        st.write('Agreed with terms!')
    if feature:
        st.write('Feature activated!')

    st.write(f'Mark: {mark}')
    st.write(f'Choose: {num}')
    st.write(f'From Start: {dts} to Finish: {dtf}')
    st.write('Alarm is set for', t)
