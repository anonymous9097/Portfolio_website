import streamlit as st

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your message here")
    submit_button = st.form_submit_button()