import streamlit as st
import pyshorteners

# Create a Streamlit app title
st.title("URL Shortener")

# Input field for the user to enter a URL
input_url = st.text_input("Enter a URL to shorten")

# Shorten the URL when the user clicks a button
if st.button("Shorten"):
    if input_url:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(input_url)
        st.success("Shortened URL: {}".format(shortened_url))
    else:
        st.warning("Please enter a URL to shorten")
