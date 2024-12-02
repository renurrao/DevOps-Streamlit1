import streamlit as st

st.title('Welcome to My App!')

with st.form('myform'):
    x = st.text_input('Please enter your name:')

    radio = st.radio('Please select your gender from the following: ', ['Male', 'Female'])

    course = st.selectbox('Please select your course: ', ['BTech', 'MCA', 'MBATech'])

    multiselect = st.multiselect('Select one or more of your hobbies from the following: ', ['Art', 'Music', 'Cooking', 'Sports'])

    date = st.date_input('Please enter your dob:')

    feedback = st.slider('Please rate us (1-5):', 1, 5)
    submitted = st.form_submit_button('Submitt my form')


if submitted:
    st.write('You entered:', x)
    st.write('You selected gender:', radio)
    st.write('You selected course:', course)
    st.write('Your hobbies are:', multiselect)
    st.write('Your dob is:', date)
    st.write('Your feedback is:', feedback)

