import streamlit as st
st.title("My Site")
st.subheader("Welcome to my site!")
st.write("Testing simple HTML <b>bold</b> and <i>italic</i> text rendering.", unsafe_allow_html=True)


st.checkbox("Subscribe to newsletter")
st.text_input("Your email address", placeholder="type here")