import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your message here")
    submit_button = st.form_submit_button("Submit")

message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""

if submit_button:
    send_email(message)
    st.info("Your email was sent successfully!")